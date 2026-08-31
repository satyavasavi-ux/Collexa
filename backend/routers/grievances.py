from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database, dependencies

router = APIRouter()

@router.get("/", response_model=List[schemas.Grievance])
async def list_grievances(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.Grievance)
    if current_user.role == models.UserRole.STUDENT:
        query = query.filter(models.Grievance.student_id == current_user.id)
    return query.order_by(models.Grievance.created_at.desc()).all()

@router.post("/", response_model=schemas.Grievance)
async def submit_grievance(
    g_in: schemas.GrievanceCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    g = models.Grievance(
        student_id=current_user.id,
        title=g_in.title,
        description=g_in.description,
        category=g_in.category,
        status="Pending"
    )
    db.add(g)
    db.commit()
    db.refresh(g)
    return g
