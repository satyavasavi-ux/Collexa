from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import datetime
import dependencies, models, database
from sqlalchemy.orm import Session

router = APIRouter()

class PredictionInput(BaseModel):
    attendance_pct: float
    internal_marks: float
    assignment_scores: float
    gpa: float

class PredictionOutput(BaseModel):
    risk_level: str
    risk_score: float
    recommendation: str

class AIQueryRequest(BaseModel):
    query: str
    context: Optional[str] = None

class AIQueryResponse(BaseModel):
    answer: str
    sources: List[str] = []
    confidence: float

@router.post("/predict", response_model=PredictionOutput)
async def predict_performance(
    input_data: PredictionInput,
    current_user: models.User = Depends(dependencies.get_current_user)
):
    # Heuristic scoring engine for academic risk classification
    weighted_score = (
        (input_data.attendance_pct * 0.3) +
        (input_data.internal_marks * 0.3) +
        (input_data.assignment_scores * 0.2) +
        (input_data.gpa * 10 * 0.2)
    )

    if weighted_score >= 80.0:
        risk = "Low Risk (High Performing)"
        rec = "Student is excelling across all metrics. Recommend advanced honors electives and research projects."
    elif weighted_score >= 60.0:
        risk = "Moderate Risk (Average)"
        rec = "Student is maintaining good standing, but should attend peer tutoring sessions to improve problem-solving speed."
    else:
        risk = "High Risk (Critical Alert)"
        rec = "Immediate academic intervention recommended. Schedule mentoring session with faculty advisor and remedial assignments."

    return {
        "risk_level": risk,
        "risk_score": round(weighted_score, 2),
        "recommendation": rec
    }

@router.post("/assistant/query", response_model=AIQueryResponse)
async def ask_campus_ai(
    req: AIQueryRequest,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    q = req.query.lower()
    
    if "attendance" in q:
        ans = "Collexa requires a minimum 75% attendance across all registered theory and laboratory courses to be eligible for End-Semester Examinations without condonation penalties."
        src = ["Academic Regulations Handbook 2024 - Section 4.2"]
    elif "fee" in q or "payment" in q:
        ans = "Tuition and hostel fees can be paid seamlessly via the Account Portal or Student Dashboard with instant GST-compliant receipt generation."
        src = ["Accounts & Finance Policy - Section 2.1"]
    elif "placement" in q or "job" in q:
        ans = "Placement drives for Fall 2026 are active. Students with a CGPA >= 7.0 and zero standing arrears are eligible to apply directly through the Placement Portal."
        src = ["Career Development & Placement Cell Guidelines"]
    elif "exam" in q or "hall ticket" in q:
        ans = "End Semester Examination Hall Tickets are issued electronically 2 weeks before commencement. Ensure your dues are cleared to download your hall ticket."
        src = ["Controller of Examinations - Autonomous Wing"]
    elif "library" in q or "book" in q:
        ans = "Students can borrow up to 3 library books simultaneously for a 14-day duration with 1 online renewal permitted prior to due date."
        src = ["Central Digital Library Catalog Policy"]
    else:
        ans = f"Collexa AI Campus Assistant: Thank you for your question regarding '{req.query}'. For personalized academic advising, please consult your department mentor or refer to the Student Handbook in your LMS portal."
        src = ["Collexa Campus Knowledge Base"]

    return {
        "answer": ans,
        "sources": src,
        "confidence": 0.95
    }

@router.get("/insights/student/{student_id}")
async def get_student_ai_insights(
    student_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    attendances = db.query(models.Attendance).filter(models.Attendance.student_id == student_id).all()
    present_cnt = sum(1 for a in attendances if a.status == "Present")
    total_att = len(attendances)
    att_pct = (present_cnt / total_att * 100) if total_att > 0 else 100.0

    marks = db.query(models.Mark).filter(models.Mark.student_id == student_id).all()
    avg_marks = (sum(m.marks_obtained for m in marks) / len(marks)) if marks else 85.0

    forecast = "Positive Trajectory - On track for Distinction" if att_pct >= 85 and avg_marks >= 80 else "Stable - Moderate Consistency"

    return {
        "student_id": student_id,
        "attendance_percentage": round(att_pct, 1),
        "average_internal_marks": round(avg_marks, 1),
        "trajectory": forecast,
        "suggested_actions": [
            "Maintain current 90%+ attendance rate in CS501 Algorithms.",
            "Complete Assignment #2 before the deadline to boost internal assessment score.",
            "Participate in the upcoming HackCollexa hackathon to gain practical portfolio experience."
        ]
    }
