from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any
from pydantic import BaseModel
import dependencies, models
from engines.proctoring_engine import ProctoringEngine

router = APIRouter()

class ProctorEvent(BaseModel):
    test_id: int
    type: str # TAB_SWITCH, NO_FACE, MULTIPLE_FACES, COPY_PASTE
    timestamp: str

class ProctorSessionSubmit(BaseModel):
    test_id: int
    student_id: int
    events: List[ProctorEvent]

@router.post("/evaluate")
async def evaluate_session(
    payload: ProctorSessionSubmit,
    current_user: models.User = Depends(dependencies.get_current_user)
):
    ev_dicts = [e.dict() for e in payload.events]
    result = ProctoringEngine.evaluate_test_session(ev_dicts)
    return {
        "test_id": payload.test_id,
        "student_id": payload.student_id,
        "evaluation": result
    }
