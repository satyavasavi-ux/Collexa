from fastapi import APIRouter, Depends
from typing import List, Dict, Any
import dependencies, models

router = APIRouter()

ALUMNI_DIRECTORY = [
    {"name": "Ananya Sharma", "batch": "Class of 2018", "company": "Google", "designation": "Staff Software Engineer", "location": "Mountain View, CA", "mentorship_open": True},
    {"name": "Karthik Raja", "batch": "Class of 2020", "company": "Microsoft", "designation": "Senior Product Manager", "location": "Seattle, WA", "mentorship_open": True},
    {"name": "Deepika Rao", "batch": "Class of 2021", "company": "Apple", "designation": "Hardware Systems Architect", "location": "Cupertino, CA", "mentorship_open": False},
    {"name": "Rohan Gupta", "batch": "Class of 2019", "company": "Y Combinator Founder", "designation": "CEO & Co-founder", "location": "Bangalore, India", "mentorship_open": True}
]

@router.get("/directory")
async def list_alumni(current_user: models.User = Depends(dependencies.get_current_user)):
    return ALUMNI_DIRECTORY
