import uuid
import datetime
import hashlib
from typing import Dict, Any

class CertificateGenerator:
    @staticmethod
    def generate_bonafide_certificate(student_name: str, roll_number: str, department: str, batch: str, academic_year: str = "2024-2025") -> Dict[str, Any]:
        cert_id = f"CERT-BONA-{uuid.uuid4().hex[:8].upper()}"
        issued_date = datetime.date.today().strftime("%d %B %Y")
        
        content = (
            f"This is to certify that {student_name} (Roll No: {roll_number}) is a bonafide student "
            f"of the Department of {department}, batch {batch}, currently pursuing undergraduate studies "
            f"at Collexa Autonomous University during the academic year {academic_year}."
        )
        
        # Compute SHA-256 Digital Verification Hash
        raw_token = f"{cert_id}|{student_name}|{roll_number}|{issued_date}"
        digital_signature = hashlib.sha256(raw_token.encode("utf-8")).hexdigest()

        return {
            "certificate_id": cert_id,
            "title": "BONAFIDE STUDENT CERTIFICATE",
            "student_name": student_name,
            "roll_number": roll_number,
            "department": department,
            "batch": batch,
            "issue_date": issued_date,
            "body_text": content,
            "digital_signature_hash": digital_signature,
            "verification_url": f"https://verify.collexa.edu/cert/{cert_id}"
        }
