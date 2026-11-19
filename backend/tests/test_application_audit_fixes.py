import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app
import seed_data
import schemas
from pydantic import ValidationError
from services.admission_service import AdmissionService

# Ensure database is seeded
seed_data.seed()

client = TestClient(app)

def get_auth_token(email="student@collexa.edu", password="student123"):
    res = client.post("/api/auth/login", json={"email": email, "password": password})
    assert res.status_code == 200
    return res.json()["access_token"]

def get_admin_token():
    res = client.post("/api/auth/login", json={"email": "admin@collexa.edu", "password": "admin123"})
    assert res.status_code == 200
    return res.json()["access_token"]

# ==========================================
# TEST 1: Reject Blank & Whitespace Inputs
# ==========================================
def test_reject_whitespace_and_empty_application():
    # ApplicationBase validation
    with pytest.raises(ValidationError):
        schemas.ApplicationCreate(
            applicant_name="   ",
            email="test@example.com",
            phone="1234567890"
        )

    with pytest.raises(ValidationError):
        schemas.ApplicationCreate(
            applicant_name="Valid Name",
            email="test@example.com",
            phone="   "
        )

    # JobApplicationBase validation
    with pytest.raises(ValidationError):
        schemas.JobApplicationCreate(
            drive_id=1,
            student_id=3,
            resume_url="   "
        )

    with pytest.raises(ValidationError):
        schemas.JobApplicationCreate(
            drive_id=1,
            student_id=3,
            resume_url="not-a-valid-url"
        )

    # AdmissionRequestBase validation
    with pytest.raises(ValidationError):
        schemas.AdmissionRequestCreate(
            first_name="  ",
            last_name="Doe",
            email="doe@example.com",
            phone_number="1234567890",
            desired_course="Computer Science"
        )

# ========================================================
# TEST 2: Prevent Duplicate Job Application (Concurrency)
# ========================================================
def test_prevent_duplicate_job_application():
    token = get_auth_token("student@collexa.edu", "student123")
    headers = {"Authorization": f"Bearer {token}"}

    # First fetch drives to find an active drive
    drives_res = client.get("/api/placements/drives", headers=headers)
    assert drives_res.status_code == 200
    drives = drives_res.json()
    assert len(drives) >= 1
    drive_id = drives[0]["id"]

    # Ensure first application is processed (or already existed)
    res1 = client.post("/api/placements/apply", json={
        "drive_id": drive_id,
        "student_id": 1,
        "resume_url": "https://drive.collexa.edu/resumes/alex_rivera_cv.pdf"
    }, headers=headers)
    assert res1.status_code in [200, 400, 409]

    # Repeated application for the same drive and student MUST be rejected (prevent duplicate)
    res2 = client.post("/api/placements/apply", json={
        "drive_id": drive_id,
        "student_id": 1,
        "resume_url": "https://drive.collexa.edu/resumes/alex_rivera_cv.pdf"
    }, headers=headers)

    assert res2.status_code in [400, 409]
    detail = res2.json().get("detail", "")
    assert "already applied" in detail.lower()

# ========================================================
# TEST 3: Duplicate Admission Request Handling
# ========================================================
def test_duplicate_admission_request_prevention():
    payload = {
        "first_name": "UniqueApplicant",
        "last_name": "Verification",
        "email": "unique.applicant.test@collexa.edu",
        "phone_number": "+1 555-9988",
        "desired_course": "Data Science & AI"
    }

    # First submission should succeed
    res1 = client.post("/api/staff/admissions", json=payload)
    assert res1.status_code in [200, 201, 409]

    # Second submission with same email and course must be rejected with 409
    res2 = client.post("/api/staff/admissions", json=payload)
    assert res2.status_code == 409
    assert "already exists" in res2.json()["detail"].lower()

# ========================================================
# TEST 4: Bounded Cache Memory in AdmissionService
# ========================================================
def test_admission_service_cache_bounding():
    service = AdmissionService()
    assert service.max_cache_size == 500

    # Execute 600 actions to test that cache never exceeds max_cache_size
    for i in range(1, 601):
        service.execute_service_action_1(entity_id=i, params={"iteration": i, "batch": "test"})

    assert len(service.cache) <= 500
