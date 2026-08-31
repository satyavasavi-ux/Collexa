from fastapi import APIRouter, Depends
import dependencies, models
from engines.certificate_generator import CertificateGenerator

router = APIRouter()

@router.get("/bonafide/{student_id}")
async def generate_bonafide(student_id: int, current_user: models.User = Depends(dependencies.get_current_user)):
    cert = CertificateGenerator.generate_bonafide_certificate(
        student_name=current_user.name,
        roll_number=current_user.student_profile.roll_number if current_user.student_profile else "COL24CS001",
        department=current_user.student_profile.department if current_user.student_profile else "Computer Science",
        batch=current_user.student_profile.batch if current_user.student_profile else "2023-2027"
    )
    return cert
