"""
Choice Based Credit System (CBCS) Matrix & Credit Allocation Module
"""
from typing import Dict, List, Any

class CBCSMatrixEngine:
    """Engine for validating student graduation credit requirements under UGC CBCS."""
    def __init__(self, regulation_year: int = 2024):
        self.regulation_year = regulation_year
        self.min_credits_required = 160

    def validate_student_credits(self, completed_credits: Dict[str, int]) -> Dict[str, Any]:
        total = sum(completed_credits.values())
        return {
            "total_credits": total,
            "is_eligible_for_degree": total >= self.min_credits_required,
            "breakdown": completed_credits
        }
