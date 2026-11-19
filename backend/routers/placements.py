from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
import datetime
import models, schemas, database, dependencies

router = APIRouter()

@router.get("/drives", response_model=List[schemas.JobDrive])
async def list_job_drives(
    status: Optional[str] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.JobDrive)
    if status:
        query = query.filter(models.JobDrive.status == status)
    return query.order_by(models.JobDrive.drive_date.desc()).all()

@router.post("/drives", response_model=schemas.JobDrive)
async def create_job_drive(
    drive_in: schemas.JobDriveCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["PLACEMENT", "ADMIN"]))
):
    drive = models.JobDrive(**drive_in.dict())
    db.add(drive)
    db.commit()
    db.refresh(drive)
    return drive

@router.post("/apply", response_model=schemas.JobApplication)
async def apply_job_drive(
    app_in: schemas.JobApplicationCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["STUDENT"]))
):
    drive = db.query(models.JobDrive).filter(models.JobDrive.id == app_in.drive_id).first()
    if not drive or drive.status != "Active":
        raise HTTPException(status_code=400, detail="Drive is not accepting applications")

    existing = db.query(models.JobApplication).filter(
        models.JobApplication.drive_id == app_in.drive_id,
        models.JobApplication.student_id == current_user.id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="You have already applied to this drive")

    clean_resume = app_in.resume_url.strip() if app_in.resume_url else "https://example.com/resume.pdf"
    app = models.JobApplication(
        drive_id=app_in.drive_id,
        student_id=current_user.id,
        resume_url=clean_resume,
        status="Applied"
    )
    try:
        db.add(app)
        db.commit()
        db.refresh(app)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="You have already applied to this drive")
    return app

@router.get("/my-applications", response_model=List[schemas.JobApplication])
async def get_my_applications(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["STUDENT"]))
):
    return db.query(models.JobApplication).filter(models.JobApplication.student_id == current_user.id).all()

@router.put("/applications/{app_id}/status")
async def update_application_status(
    app_id: int,
    status: str,
    feedback: Optional[str] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["PLACEMENT", "ADMIN"]))
):
    app = db.query(models.JobApplication).filter(models.JobApplication.id == app_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    app.status = status
    if feedback:
        app.feedback = feedback
    db.commit()
    return {"message": "Application status updated successfully"}
