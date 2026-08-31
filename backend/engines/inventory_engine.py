from typing import List, Dict, Any
import datetime

class AssetManager:
    @staticmethod
    def audit_equipment_lifecycle(purchase_date: datetime.date, expected_life_years: int, original_cost: float, depreciation_rate: float = 0.15) -> Dict[str, Any]:
        today = datetime.date.today()
        years_used = (today - purchase_date).days / 365.25
        current_value = original_cost * ((1.0 - depreciation_rate) ** years_used)
        current_value = max(0.0, current_value)

        health_status = "Good Condition"
        if years_used > expected_life_years:
            health_status = "Due for Scrap / Replacement"
        elif years_used > (expected_life_years * 0.75):
            health_status = "Maintenance Inspection Required"

        return {
            "years_in_service": round(years_used, 1),
            "original_cost": round(original_cost, 2),
            "depreciated_book_value": round(current_value, 2),
            "lifecycle_status": health_status,
            "salvage_estimate": round(original_cost * 0.05, 2)
        }
