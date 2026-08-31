from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
import datetime
import uuid
import models, schemas, database, dependencies

router = APIRouter()

@router.get("/", response_model=List[schemas.CampusEvent])
async def list_events(
    category: Optional[str] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.CampusEvent)
    if category:
        query = query.filter(models.CampusEvent.category == category)
    return query.order_by(models.CampusEvent.start_time.asc()).all()

@router.post("/", response_model=schemas.CampusEvent)
async def create_event(
    event_in: schemas.CampusEventCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["ADMIN", "TEACHER"]))
):
    event = models.CampusEvent(**event_in.dict())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

@router.post("/{event_id}/register", response_model=schemas.EventRegistration)
async def register_for_event(
    event_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    event = db.query(models.CampusEvent).filter(models.CampusEvent.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    existing = db.query(models.EventRegistration).filter(
        models.EventRegistration.event_id == event_id,
        models.EventRegistration.user_id == current_user.id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already registered for this event")

    ticket_code = f"EVT-{event_id}-{uuid.uuid4().hex[:6].upper()}"
    reg = models.EventRegistration(
        event_id=event_id,
        user_id=current_user.id,
        ticket_code=ticket_code,
        payment_status="Free" if event.registration_fee <= 0 else "Paid",
        attendance_status="Registered"
    )
    db.add(reg)
    db.commit()
    db.refresh(reg)
    return reg

@router.get("/my-tickets", response_model=List[schemas.EventRegistration])
async def get_my_tickets(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    return db.query(models.EventRegistration).filter(models.EventRegistration.user_id == current_user.id).all()
