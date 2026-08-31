from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, database, dependencies, datetime

router = APIRouter()

@router.get("/hall-tickets", response_model=List[schemas.ExamHallTicket])
async def list_hall_tickets(
    student_id: Optional[int] = None,
    semester: Optional[int] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.ExamHallTicket)
    if current_user.role == models.UserRole.STUDENT:
        query = query.filter(models.ExamHallTicket.student_id == current_user.id)
    elif student_id:
        query = query.filter(models.ExamHallTicket.student_id == student_id)
    if semester:
        query = query.filter(models.ExamHallTicket.semester == semester)
    return query.all()

@router.post("/hall-tickets/generate")
async def generate_hall_ticket(
    ticket_in: schemas.ExamHallTicketCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["EXAM", "ADMIN"]))
):
    existing = db.query(models.ExamHallTicket).filter(
        models.ExamHallTicket.student_id == ticket_in.student_id,
        models.ExamHallTicket.semester == ticket_in.semester,
        models.ExamHallTicket.exam_name == ticket_in.exam_name
    ).first()
    if existing:
        return existing

    ticket = models.ExamHallTicket(**ticket_in.dict())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

@router.get("/results/student/{student_id}")
async def get_student_transcript(
    student_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    if current_user.role == models.UserRole.STUDENT and current_user.id != student_id:
        raise HTTPException(status_code=403, detail="Unauthorized to view other students' results")

    student = db.query(models.User).filter(models.User.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    marks = db.query(models.Mark).filter(
        models.Mark.student_id == student_id,
        models.Mark.status == "Published"
    ).all()

    total_marks = sum(m.marks_obtained for m in marks)
    total_max = sum(m.max_marks for m in marks)
    percentage = (total_marks / total_max * 100) if total_max > 0 else 0.0

    # Calculate GPA estimate (scale of 10)
    gpa = round(min(10.0, (percentage / 10.0) + 0.5), 2) if total_max > 0 else 0.0

    return {
        "student_id": student.id,
        "student_name": student.name,
        "roll_number": student.student_profile.roll_number if student.student_profile else "N/A",
        "department": student.student_profile.department if student.student_profile else "N/A",
        "semester": student.student_profile.semester if student.student_profile else 1,
        "marks": marks,
        "total_obtained": total_marks,
        "total_max": total_max,
        "percentage": round(percentage, 2),
        "gpa": gpa
    }

@router.post("/publish-results")
async def publish_results(
    semester: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["EXAM", "ADMIN"]))
):
    draft_marks = db.query(models.Mark).filter(models.Mark.semester == semester).all()
    count = 0
    for m in draft_marks:
        m.status = "Published"
        count += 1
    db.commit()
    return {"message": f"Successfully published {count} mark entries for Semester {semester}."}
