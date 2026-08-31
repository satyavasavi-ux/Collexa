import datetime
from decimal import Decimal
from database import SessionLocal, engine, Base
import models, auth

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Check if admin already exists
    if db.query(models.User).filter(models.User.email == "admin@collexa.edu").first():
        print("Database already seeded. Skipping initial creation.")
        db.close()
        return

    print("Seeding demo data for Collexa ERP...")

    # 1. Users
    admin_user = models.User(
        name="Dr. Eleanor Vance",
        email="admin@collexa.edu",
        hashed_password=auth.get_password_hash("admin123"),
        role=models.UserRole.ADMIN,
        phone_number="+1 555-0199",
        avatar_url="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150"
    )
    db.add(admin_user)
    db.flush()
    db.add(models.Admin(user_id=admin_user.id, department="Administration", access_level="SUPER_ADMIN"))

    teacher_user = models.User(
        name="Prof. Alan Turing",
        email="teacher@collexa.edu",
        hashed_password=auth.get_password_hash("teacher123"),
        role=models.UserRole.TEACHER,
        phone_number="+1 555-0144",
        avatar_url="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150"
    )
    db.add(teacher_user)
    db.flush()
    db.add(models.Teacher(
        user_id=teacher_user.id,
        employee_code="EMP-1001",
        department="Computer Science",
        designation="Professor & Head",
        qualification="Ph.D in Computing",
        experience_years=12.5,
        specialization="Algorithms & Machine Learning"
    ))

    student_user = models.User(
        name="Alex Rivera",
        email="student@collexa.edu",
        hashed_password=auth.get_password_hash("student123"),
        role=models.UserRole.STUDENT,
        phone_number="+1 555-0188",
        avatar_url="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150"
    )
    db.add(student_user)
    db.flush()
    student_profile = models.Student(
        user_id=student_user.id,
        roll_number="COL24CS001",
        department="Computer Science",
        year=3,
        semester=5,
        section="A",
        batch="2023-2027",
        phone_number="+1 555-0188",
        guardian_name="Marcus Rivera",
        guardian_phone="+1 555-0189",
        blood_group="O+",
        cgpa=8.85,
        credits_completed=92
    )
    db.add(student_profile)

    admission_user = models.User(
        name="Sarah Jenkins",
        email="admission@collexa.edu",
        hashed_password=auth.get_password_hash("admission123"),
        role=models.UserRole.ADMISSION,
        phone_number="+1 555-0166"
    )
    db.add(admission_user)
    db.flush()
    db.add(models.AdmissionStaff(user_id=admission_user.id, employee_id="ADM-001"))

    exam_user = models.User(
        name="Dr. Robert Thorne",
        email="exam@collexa.edu",
        hashed_password=auth.get_password_hash("exam123"),
        role=models.UserRole.EXAM,
        phone_number="+1 555-0177"
    )
    db.add(exam_user)
    db.flush()
    db.add(models.ExamStaff(user_id=exam_user.id, employee_id="EXM-001"))

    account_user = models.User(
        name="Claire Sterling",
        email="account@collexa.edu",
        hashed_password=auth.get_password_hash("account123"),
        role=models.UserRole.ACCOUNT,
        phone_number="+1 555-0155"
    )
    db.add(account_user)
    db.flush()
    db.add(models.AccountStaff(user_id=account_user.id, employee_id="ACC-001"))

    # 2. Subjects
    subj1 = models.Subject(code="CS501", name="Design & Analysis of Algorithms", department="Computer Science", semester=5, credits=4, hours_per_week=4)
    subj2 = models.Subject(code="CS502", name="Database Management Systems", department="Computer Science", semester=5, credits=4, hours_per_week=4)
    subj3 = models.Subject(code="CS503", name="Operating Systems & Architecture", department="Computer Science", semester=5, credits=3, hours_per_week=3)
    subj4 = models.Subject(code="CS504", name="Computer Networks & Security", department="Computer Science", semester=5, credits=3, hours_per_week=3)
    subj5 = models.Subject(code="AI505", name="Machine Learning Fundamentals", department="Computer Science", semester=5, credits=4, hours_per_week=4)
    db.add_all([subj1, subj2, subj3, subj4, subj5])
    db.flush()

    # 3. Timetable Entries
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i, day in enumerate(days):
        db.add(models.TimetableEntry(
            department="Computer Science",
            year=3,
            section="A",
            semester=5,
            day_of_week=day,
            hour_slot=1,
            subject_id=subj1.id,
            teacher_id=teacher_user.id,
            room_number="Hall-301"
        ))
        db.add(models.TimetableEntry(
            department="Computer Science",
            year=3,
            section="A",
            semester=5,
            day_of_week=day,
            hour_slot=2,
            subject_id=subj2.id,
            teacher_id=teacher_user.id,
            room_number="Lab-B"
        ))

    # 4. Attendance
    today = datetime.date.today()
    for d in range(15):
        past_date = today - datetime.timedelta(days=d)
        db.add(models.Attendance(
            student_id=student_user.id,
            subject_id=subj1.id,
            teacher_id=teacher_user.id,
            date=past_date,
            hour_slot=1,
            status="Present" if d % 7 != 0 else "Absent"
        ))

    # 5. Marks
    db.add(models.Mark(
        student_id=student_user.id,
        subject_id=subj1.id,
        teacher_id=teacher_user.id,
        exam_type="Mid-Term",
        semester=5,
        marks_obtained=92.0,
        max_marks=100.0,
        grade="O",
        remarks="Exceptional algorithmic problem solving."
    ))
    db.add(models.Mark(
        student_id=student_user.id,
        subject_id=subj2.id,
        teacher_id=teacher_user.id,
        exam_type="Mid-Term",
        semester=5,
        marks_obtained=88.5,
        max_marks=100.0,
        grade="A+",
        remarks="Great query optimization and schema design."
    ))

    # 6. Fees & Payments
    fee_rec = models.Fee(
        student_id=student_user.id,
        fee_type="Semester 5 Tuition & Lab Fee",
        academic_year="2024-2025",
        semester=5,
        total_amount=Decimal("65000.00"),
        paid_amount=Decimal("45000.00"),
        due_amount=Decimal("20000.00"),
        due_date=today + datetime.timedelta(days=30),
        status="Partial"
    )
    db.add(fee_rec)
    db.flush()
    db.add(models.FeePayment(
        fee_id=fee_rec.id,
        amount=Decimal("45000.00"),
        payment_method="Online NetBanking",
        transaction_id="TXN-2024-998822",
        receipt_number="RCPT-00912",
        status="Completed",
        notes="First installment received"
    ))

    # 7. Library Books
    b1 = models.Book(isbn="978-0131103627", title="The C Programming Language", author="Kernighan & Ritchie", category="Computer Science", total_copies=10, available_copies=8, rack_location="CS-A-01")
    b2 = models.Book(isbn="978-0262033848", title="Introduction to Algorithms (CLRS)", author="Cormen, Leiserson, Rivest, Stein", category="Computer Science", total_copies=15, available_copies=12, rack_location="CS-A-04")
    b3 = models.Book(isbn="978-0134685991", title="Effective Java (3rd Ed)", author="Joshua Bloch", category="Software Engineering", total_copies=8, available_copies=6, rack_location="CS-B-02")
    b4 = models.Book(isbn="978-0596007126", title="Head First Design Patterns", author="Eric Freeman", category="Software Architecture", total_copies=12, available_copies=10, rack_location="CS-B-05")
    db.add_all([b1, b2, b3, b4])
    db.flush()

    db.add(models.BookBorrow(
        book_id=b2.id,
        user_id=student_user.id,
        borrow_date=today - datetime.timedelta(days=5),
        due_date=today + datetime.timedelta(days=9),
        status="Issued"
    ))

    # 8. Hostels & Bus Routes
    hostel = models.Hostel(name="Evergreen Hall of Residence", type="Boys", warden_name="Dr. Vikram Sen", total_rooms=80)
    db.add(hostel)
    db.flush()
    room = models.HostelRoom(hostel_id=hostel.id, room_number="B-204", floor=2, capacity=2, occupied_count=1)
    db.add(room)
    db.flush()
    student_profile.hostel_room_id = room.id

    route = models.BusRoute(
        route_number="RT-08",
        route_name="North Metro Express - Campus Line",
        start_point="Central Metro Station",
        end_point="Collexa Main Campus",
        driver_name="Ravi Shankar",
        driver_phone="+1 555-0988",
        departure_time="07:45 AM"
    )
    db.add(route)
    db.flush()
    student_profile.bus_route_id = route.id

    # 9. Placement Drives
    d1 = models.JobDrive(
        company_name="Google",
        job_title="Software Development Engineer",
        job_description="Join the Cloud and AI infrastructure team building next-gen scalable distributed systems.",
        eligibility_cgpa=8.0,
        salary_package="32 LPA",
        drive_date=today + datetime.timedelta(days=20),
        registration_deadline=today + datetime.timedelta(days=10),
        location="Bangalore / Hybrid",
        status="Active"
    )
    d2 = models.JobDrive(
        company_name="Microsoft",
        job_title="Core Systems Software Engineer",
        job_description="Developing Azure intelligent cloud backend and edge compute microservices.",
        eligibility_cgpa=7.5,
        salary_package="28 LPA",
        drive_date=today + datetime.timedelta(days=28),
        registration_deadline=today + datetime.timedelta(days=15),
        location="Hyderabad / Remote",
        status="Active"
    )
    db.add_all([d1, d2])
    db.flush()

    db.add(models.JobApplication(
        drive_id=d1.id,
        student_id=student_user.id,
        resume_url="https://drive.collexa.edu/resumes/alex_rivera_cv.pdf",
        status="Shortlisted",
        feedback="Shortlisted for Technical Round 1 on 15th next month."
    ))

    # 10. Campus Events & Clubs
    evt1 = models.CampusEvent(
        title="HackCollexa 2026 - 36hr National Hackathon",
        description="Build transformative AI, Web3, and IoT solutions with $25,000+ in grand prizes.",
        category="Technical",
        organizer="ACM Student Chapter & GDSC",
        start_time=datetime.datetime.utcnow() + datetime.timedelta(days=12),
        end_time=datetime.datetime.utcnow() + datetime.timedelta(days=14),
        venue="Collexa Tech Center & Innovation Pavilion",
        max_participants=500
    )
    evt2 = models.CampusEvent(
        title="Annual Cultural Extravaganza: Aurora Fest",
        description="Music concerts, dramatic plays, art showcases, and celebrity performances.",
        category="Cultural",
        organizer="Cultural Council",
        start_time=datetime.datetime.utcnow() + datetime.timedelta(days=25),
        end_time=datetime.datetime.utcnow() + datetime.timedelta(days=27),
        venue="Open Air Amphitheatre"
    )
    db.add_all([evt1, evt2])
    db.flush()

    # 11. Chat Channels & Messages
    ch1 = models.ChatChannel(name="General Campus Forum", description="All campus students and faculty general discussion", is_private=False)
    ch2 = models.ChatChannel(name="Computer Science 2027", description="Class of 2027 CS batch discussion and course study notes", is_private=False)
    ch3 = models.ChatChannel(name="Placement Preparation & Coding", description="DSA, LeetCode, and mock interview discussion group", is_private=False)
    db.add_all([ch1, ch2, ch3])
    db.flush()

    db.add(models.ChatMessage(channel_id=ch1.id, sender_id=admin_user.id, content="Welcome to Collexa Enterprise ERP! All services and portals are fully live."))
    db.add(models.ChatMessage(channel_id=ch2.id, sender_id=teacher_user.id, content="Please note that Algorithm Assignment #2 is due next Monday at 11:59 PM."))
    db.add(models.ChatMessage(channel_id=ch2.id, sender_id=student_user.id, content="Thank you Professor, we are submitting our solutions today."))

    # 12. Hall Ticket
    db.add(models.ExamHallTicket(
        student_id=student_user.id,
        exam_name="End Semester Autonomous Theory Exams - Fall 2026",
        semester=5,
        hall_ticket_number="HT-2026-CS-00192",
        issue_date=today,
        seat_number="Block-C, Room 204, Desk 12",
        center_name="Main Academic Complex",
        status="Issued"
    ))

    # 13. Notifications
    db.add(models.Notification(
        student_id=student_user.id,
        user_id=student_user.id,
        title="Hall Ticket Published",
        message="Your Hall Ticket for Fall 2026 End Semester Examinations is now available for download.",
        category="Exam",
        priority="High"
    ))
    db.add(models.Notification(
        student_id=student_user.id,
        user_id=student_user.id,
        title="Google SDE Drive Shortlist",
        message="Congratulations! You have been shortlisted for Google Technical Round 1.",
        category="Placement",
        priority="Urgent"
    ))

    db.commit()
    db.close()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed()
