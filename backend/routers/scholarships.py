from fastapi import APIRouter, Depends
from typing import List, Dict, Any
import dependencies, models

router = APIRouter()

SCHOLARSHIPS = [
    {"id": 1, "title": "Merit Academic Excellence Award", "amount": "₹50,000 / Year", "criteria": "CGPA ≥ 9.0 in previous academic year", "deadline": "2026-10-31", "provider": "University Endowment Fund"},
    {"id": 2, "title": "Women in Technology & STEM Grant", "amount": "₹75,000 / Year", "criteria": "Female engineering students with CGPA ≥ 8.0", "deadline": "2026-11-15", "provider": "Global Tech Foundation"},
    {"id": 3, "title": "First Generation Graduate Assistance", "amount": "100% Tuition Waiver", "criteria": "Family annual income < ₹3,00,000", "deadline": "2026-10-15", "provider": "Higher Education Ministry"}
]

@router.get("/")
async def get_scholarships(current_user: models.User = Depends(dependencies.get_current_user)):
    return SCHOLARSHIPS
