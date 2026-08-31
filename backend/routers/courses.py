from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, database, dependencies, datetime

router = APIRouter()

@router.get("/subjects", response_model=List[schemas.Subject])
async def list_subjects(
    department: Optional[str] = None,
    semester: Optional[int] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.Subject)
    if department:
        query = query.filter(models.Subject.department == department)
    if semester:
        query = query.filter(models.Subject.semester == semester)
    return query.all()

@router.post("/subjects", response_model=schemas.Subject)
async def create_subject(
    subject_in: schemas.SubjectCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["ADMIN", "TEACHER"]))
):
    existing = db.query(models.Subject).filter(models.Subject.code == subject_in.code).first()
    if existing:
        raise HTTPException(status_code=400, detail="Subject code already exists")
    db_subj = models.Subject(**subject_in.dict())
    db.add(db_subj)
    db.commit()
    db.refresh(db_subj)
    return db_subj

@router.get("/subjects/{subject_id}/modules", response_model=List[schemas.CourseModule])
async def get_modules(
    subject_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    return db.query(models.CourseModule).filter(models.CourseModule.subject_id == subject_id).order_by(models.CourseModule.module_number).all()

@router.post("/subjects/{subject_id}/modules", response_model=schemas.CourseModule)
async def add_module(
    subject_id: int,
    module_in: schemas.CourseModuleCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["TEACHER", "ADMIN"]))
):
    mod = models.CourseModule(**module_in.dict())
    db.add(mod)
    db.commit()
    db.refresh(mod)
    return mod

@router.get("/assignments", response_model=List[schemas.Assignment])
async def get_assignments(
    subject_id: Optional[int] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.Assignment)
    if subject_id:
        query = query.filter(models.Assignment.subject_id == subject_id)
    return query.order_by(models.Assignment.due_date.desc()).all()

@router.post("/assignments", response_model=schemas.Assignment)
async def create_assignment(
    assignment_in: schemas.AssignmentCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["TEACHER", "ADMIN"]))
):
    db_assign = models.Assignment(
        subject_id=assignment_in.subject_id,
        teacher_id=current_user.id,
        title=assignment_in.title,
        description=assignment_in.description,
        due_date=assignment_in.due_date,
        max_points=assignment_in.max_points,
        attachment_url=assignment_in.attachment_url
    )
    db.add(db_assign)
    db.commit()
    db.refresh(db_assign)
    return db_assign

@router.get("/assignments/{assignment_id}/submissions", response_model=List[schemas.Submission])
async def get_submissions(
    assignment_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["TEACHER", "ADMIN"]))
):
    return db.query(models.Submission).filter(models.Submission.assignment_id == assignment_id).all()

@router.post("/assignments/{assignment_id}/submit", response_model=schemas.Submission)
async def submit_assignment(
    assignment_id: int,
    submission_in: schemas.SubmissionCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["STUDENT"]))
):
    assign = db.query(models.Assignment).filter(models.Assignment.id == assignment_id).first()
    if not assign:
        raise HTTPException(status_code=404, detail="Assignment not found")

    existing = db.query(models.Submission).filter(
        models.Submission.assignment_id == assignment_id,
        models.Submission.student_id == current_user.id
    ).first()

    status_val = "Late" if datetime.datetime.utcnow() > assign.due_date else "Submitted"

    if existing:
        existing.submission_text = submission_in.submission_text
        existing.file_url = submission_in.file_url
        existing.submitted_at = datetime.datetime.utcnow()
        existing.status = status_val
        db.commit()
        db.refresh(existing)
        return existing

    sub = models.Submission(
        assignment_id=assignment_id,
        student_id=current_user.id,
        submission_text=submission_in.submission_text,
        file_url=submission_in.file_url,
        status=status_val
    )
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub

@router.put("/submissions/{submission_id}/grade", response_model=schemas.Submission)
async def grade_submission(
    submission_id: int,
    grade_in: schemas.SubmissionGrade,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["TEACHER", "ADMIN"]))
):
    sub = db.query(models.Submission).filter(models.Submission.id == submission_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Submission not found")
    sub.marks_awarded = grade_in.marks_awarded
    sub.feedback = grade_in.feedback
    sub.status = "Graded"
    db.commit()
    db.refresh(sub)
    return sub
