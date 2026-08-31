from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal
import datetime
import models, schemas, database, dependencies
from websocket_manager import manager

router = APIRouter()

@router.get("/summary")
async def get_finance_overview(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["ACCOUNT", "ADMIN"]))
):
    fees = db.query(models.Fee).all()
    total_billed = sum(f.total_amount for f in fees)
    total_collected = sum(f.paid_amount for f in fees)
    total_due = sum(f.due_amount for f in fees)
    total_payments = db.query(models.FeePayment).count()

    return {
        "total_billed": total_billed,
        "total_collected": total_collected,
        "total_due": total_due,
        "collection_rate": round(float(total_collected / total_billed * 100), 2) if total_billed > 0 else 0.0,
        "transaction_count": total_payments
    }

@router.get("/fees", response_model=List[schemas.Fee])
async def list_fees(
    student_id: Optional[int] = None,
    status: Optional[str] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.Fee)
    if current_user.role == models.UserRole.STUDENT:
        query = query.filter(models.Fee.student_id == current_user.id)
    elif student_id:
        query = query.filter(models.Fee.student_id == student_id)
    if status:
        query = query.filter(models.Fee.status == status)
    return query.all()

@router.post("/invoices/generate")
async def generate_invoice(
    fee_in: schemas.FeeCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["ACCOUNT", "ADMIN"]))
):
    fee = models.Fee(**fee_in.dict())
    db.add(fee)
    db.commit()
    db.refresh(fee)
    return fee

@router.post("/payments/record", response_model=schemas.FeePayment)
async def record_payment(
    payment_in: schemas.FeePaymentCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["ACCOUNT", "ADMIN"]))
):
    fee = db.query(models.Fee).filter(models.Fee.id == payment_in.fee_id).first()
    if not fee:
        raise HTTPException(status_code=404, detail="Fee invoice not found")

    receipt_no = payment_in.receipt_number or f"RCPT-{datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
    
    payment = models.FeePayment(
        fee_id=payment_in.fee_id,
        amount=payment_in.amount,
        payment_method=payment_in.payment_method,
        transaction_id=payment_in.transaction_id or f"TXN{datetime.datetime.utcnow().timestamp():.0f}",
        receipt_number=receipt_no,
        status="Completed",
        notes=payment_in.notes
    )
    db.add(payment)

    fee.paid_amount += payment_in.amount
    fee.due_amount = max(Decimal("0.00"), fee.total_amount - fee.paid_amount)
    if fee.due_amount <= Decimal("0.00"):
        fee.status = "Paid"
    else:
        fee.status = "Partial"

    db.commit()
    db.refresh(payment)
    await manager.broadcast({"type": "PAYMENT_RECORDED", "receipt": receipt_no, "amount": str(payment_in.amount)})
    return payment

@router.get("/payments/recent", response_model=List[schemas.FeePayment])
async def get_recent_payments(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["ACCOUNT", "ADMIN"]))
):
    return db.query(models.FeePayment).order_by(models.FeePayment.payment_date.desc()).limit(50).all()
