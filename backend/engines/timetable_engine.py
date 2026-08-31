import random
from typing import List, Dict, Any, Tuple

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
SLOTS = [1, 2, 3, 4, 5, 6, 7, 8]

class TimetableScheduler:
    def __init__(self, subjects: List[Dict[str, Any]], teachers: List[Dict[str, Any]], rooms: List[str]):
        self.subjects = subjects
        self.teachers = teachers
        self.rooms = rooms

    def generate_conflict_free_schedule(self, department: str, year: int, section: str, semester: int) -> List[Dict[str, Any]]:
        schedule = []
        occupied_teacher_slots = set() # (teacher_id, day, slot)
        occupied_room_slots = set()    # (room, day, slot)

        dept_subjects = [s for s in self.subjects if s.get("department") == department or s.get("semester") == semester]
        if not dept_subjects:
            dept_subjects = self.subjects[:5]

        for day in DAYS[:5]: # 5 weekdays
            for slot in SLOTS[:6]: # 6 periods a day
                # Pick a subject in round-robin / random
                subject = random.choice(dept_subjects)
                teacher = random.choice(self.teachers) if self.teachers else {"id": 1, "name": "Faculty"}
                room = random.choice(self.rooms) if self.rooms else "Room-101"

                # Check conflict
                if (teacher.get("id"), day, slot) not in occupied_teacher_slots and (room, day, slot) not in occupied_room_slots:
                    occupied_teacher_slots.add((teacher.get("id"), day, slot))
                    occupied_room_slots.add((room, day, slot))
                    
                    schedule.append({
                        "department": department,
                        "year": year,
                        "section": section,
                        "semester": semester,
                        "day_of_week": day,
                        "hour_slot": slot,
                        "subject_id": subject.get("id", 1),
                        "subject_name": subject.get("name", "Algorithms"),
                        "subject_code": subject.get("code", "CS101"),
                        "teacher_id": teacher.get("id", 1),
                        "teacher_name": teacher.get("name", "Dr. Vance"),
                        "room_number": room
                    })
        return schedule
