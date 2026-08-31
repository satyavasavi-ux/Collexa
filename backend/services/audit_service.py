import datetime
from sqlalchemy.orm import Session
import models

def log_action(db: Session, user_id: int, action: str, entity: str, entity_id: str, details: str = "", ip_address: str = "127.0.0.1"):
    log = models.AuditLog(
        user_id=user_id,
        action=action,
        entity=entity,
        entity_id=str(entity_id),
        details=details,
        ip_address=ip_address,
        timestamp=datetime.datetime.utcnow()
    )
    db.add(log)
    db.commit()
