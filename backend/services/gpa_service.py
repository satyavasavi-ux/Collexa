from typing import List, Dict, Any

GRADE_POINTS = {
    "O": 10.0,
    "A+": 9.0,
    "A": 8.0,
    "B+": 7.0,
    "B": 6.0,
    "C": 5.0,
    "P": 4.0,
    "F": 0.0,
    "AB": 0.0
}

def calculate_gpa(marks_records: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not marks_records:
        return {"gpa": 0.0, "total_credits": 0, "status": "Incomplete"}
    
    total_credit_points = 0.0
    total_credits = 0

    for m in marks_records:
        credits = m.get("credits", 3)
        grade = m.get("grade", "A")
        pts = GRADE_POINTS.get(grade, 8.0)
        total_credit_points += (pts * credits)
        total_credits += credits

    gpa = round(total_credit_points / total_credits, 2) if total_credits > 0 else 0.0
    return {
        "gpa": gpa,
        "total_credits": total_credits,
        "grade_points": total_credit_points,
        "classification": "First Class with Distinction" if gpa >= 8.5 else ("First Class" if gpa >= 6.5 else "Second Class")
    }
