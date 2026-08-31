from fastapi import APIRouter, Depends
import datetime
from typing import List, Dict, Any
import dependencies, models
from engines.inventory_engine import AssetManager

router = APIRouter()

ASSET_REGISTRY = [
    {"id": 1, "name": "Dell Precision Workstations (Lab A)", "category": "Computers", "purchase_date": datetime.date(2023, 6, 1), "life_years": 5, "cost": 1250000.0},
    {"id": 2, "name": "Keysight Digital Oscilloscopes", "category": "ECE Labs", "purchase_date": datetime.date(2022, 1, 15), "life_years": 8, "cost": 450000.0},
    {"id": 3, "name": "Cisco Catalyst Core Switches", "category": "Network Center", "purchase_date": datetime.date(2021, 8, 20), "life_years": 6, "cost": 890000.0},
    {"id": 4, "name": "NVIDIA A100 AI Compute Node", "category": "Research Center", "purchase_date": datetime.date(2024, 2, 10), "life_years": 4, "cost": 2400000.0}
]

@router.get("/assets")
async def list_assets(current_user: models.User = Depends(dependencies.RoleChecker(["ADMIN", "ACCOUNT"]))):
    audited = []
    for a in ASSET_REGISTRY:
        audit = AssetManager.audit_equipment_lifecycle(a["purchase_date"], a["life_years"], a["cost"])
        audited.append({**a, **audit})
    return audited
