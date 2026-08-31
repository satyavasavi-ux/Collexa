import datetime
from typing import Dict, Any, List

class ProctoringEngine:
    @staticmethod
    def evaluate_test_session(events: List[Dict[str, Any]]) -> Dict[str, Any]:
        tab_switches = 0
        face_not_visible_count = 0
        multiple_faces_detected = 0
        suspicious_keystrokes = 0

        for evt in events:
            evt_type = evt.get("type", "")
            if evt_type == "TAB_SWITCH":
                tab_switches += 1
            elif evt_type == "NO_FACE":
                face_not_visible_count += 1
            elif evt_type == "MULTIPLE_FACES":
                multiple_faces_detected += 1
            elif evt_type == "COPY_PASTE":
                suspicious_keystrokes += 1

        integrity_score = 100 - (tab_switches * 10) - (face_not_visible_count * 5) - (multiple_faces_detected * 20) - (suspicious_keystrokes * 5)
        integrity_score = max(0, min(100, integrity_score))

        status = "Clean"
        if integrity_score < 60:
            status = "Flagged for Human Review (High Infractions)"
        elif integrity_score < 80:
            status = "Moderate Warnings"

        return {
            "integrity_score": integrity_score,
            "status": status,
            "metrics": {
                "tab_switches": tab_switches,
                "face_absent_incidents": face_not_visible_count,
                "multiple_faces_incidents": multiple_faces_detected,
                "copy_paste_attempts": suspicious_keystrokes
            }
        }
