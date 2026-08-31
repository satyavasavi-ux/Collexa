from fastapi import APIRouter, Depends
from decimal import Decimal
from typing import Optional
import dependencies, models
from engines.payroll_engine import PayrollCalculator

router = APIRouter()

@router.get("/slip/{employee_id}")
async def get_salary_slip(
    employee_id: str,
    basic_pay: Optional[Decimal] = Decimal("65000.00"),
    days_present: Optional[int] = 30,
    current_user: models.User = Depends(dependencies.RoleChecker(["ACCOUNT", "ADMIN", "TEACHER"]))
):
    slip = PayrollCalculator.generate_salary_slip(
        employee_id=employee_id,
        employee_name=current_user.name,
        designation="Senior Faculty / Specialist",
        basic_pay=basic_pay,
        days_present=days_present
    )
    return slip
