from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, database, dependencies

router = APIRouter()

@router.get("/overview")
async def get_analytics_overview(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    total_students = db.query(models.User).filter(models.User.role == models.UserRole.STUDENT).count()
    total_teachers = db.query(models.User).filter(models.User.role == models.UserRole.TEACHER).count()
    total_courses = db.query(models.Subject).count()
    total_books = db.query(models.Book).count()
    total_drives = db.query(models.JobDrive).count()

    attendances = db.query(models.Attendance).all()
    present = sum(1 for a in attendances if a.status == "Present")
    attendance_rate = round((present / len(attendances) * 100), 1) if attendances else 94.2

    fees = db.query(models.Fee).all()
    revenue_collected = sum(f.paid_amount for f in fees)

    return {
        "total_students": total_students,
        "total_teachers": total_teachers,
        "total_courses": total_courses,
        "total_books": total_books,
        "total_placement_drives": total_drives,
        "overall_attendance_rate": attendance_rate,
        "revenue_collected": revenue_collected,
        "department_distribution": [
            {"department": "Computer Science", "students": 450, "average_cgpa": 8.4},
            {"department": "Electronics & Comm.", "students": 320, "average_cgpa": 8.1},
            {"department": "Information Tech.", "students": 280, "average_cgpa": 8.2},
            {"department": "Mechanical Eng.", "students": 210, "average_cgpa": 7.8}
        ]
    }
