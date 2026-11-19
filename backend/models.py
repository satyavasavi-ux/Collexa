import enum
import datetime
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, Date, ForeignKey, 
    Text, Enum, Numeric, UniqueConstraint
)
from sqlalchemy.orm import relationship
from database import Base

class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"
    ADMISSION = "ADMISSION"
    EXAM = "EXAM"
    ACCOUNT = "ACCOUNT"
    LIBRARY = "LIBRARY"
    PLACEMENT = "PLACEMENT"
    HOSTEL = "HOSTEL"
    TRANSPORT = "TRANSPORT"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.STUDENT)
    phone_number = Column(String(20), nullable=True)
    avatar_url = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Profiles
    student_profile = relationship("Student", back_populates="user", uselist=False, cascade="all, delete-orphan")
    teacher_profile = relationship("Teacher", back_populates="user", uselist=False, cascade="all, delete-orphan")
    admin_profile = relationship("Admin", back_populates="user", uselist=False, cascade="all, delete-orphan")
    admission_profile = relationship("AdmissionStaff", back_populates="user", uselist=False, cascade="all, delete-orphan")
    exam_profile = relationship("ExamStaff", back_populates="user", uselist=False, cascade="all, delete-orphan")
    account_profile = relationship("AccountStaff", back_populates="user", uselist=False, cascade="all, delete-orphan")

    # Direct User Activities
    notifications = relationship("Notification", back_populates="user", foreign_keys="Notification.user_id", cascade="all, delete-orphan")
    sent_messages = relationship("ChatMessage", back_populates="sender", cascade="all, delete-orphan")
    book_borrows = relationship("BookBorrow", back_populates="user", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLog", back_populates="user")
    attendances = relationship("Attendance", back_populates="student_user", foreign_keys="Attendance.student_id", cascade="all, delete-orphan")
    marks = relationship("Mark", back_populates="student_user", foreign_keys="Mark.student_id", cascade="all, delete-orphan")
    fees = relationship("Fee", back_populates="student_user", foreign_keys="Fee.student_id", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    roll_number = Column(String(50), unique=True, index=True, nullable=True)
    department = Column(String(100), default="Computer Science")
    year = Column(Integer, default=1)
    semester = Column(Integer, default=1)
    section = Column(String(10), default="A")
    batch = Column(String(20), default="2023-2027")
    phone_number = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    guardian_name = Column(String(150), nullable=True)
    guardian_phone = Column(String(20), nullable=True)
    blood_group = Column(String(10), nullable=True)
    dob = Column(Date, nullable=True)
    admission_date = Column(Date, default=datetime.date.today)
    cgpa = Column(Float, default=0.0)
    credits_completed = Column(Integer, default=0)
    hostel_room_id = Column(Integer, ForeignKey("hostel_rooms.id", ondelete="SET NULL"), nullable=True)
    bus_route_id = Column(Integer, ForeignKey("bus_routes.id", ondelete="SET NULL"), nullable=True)

    user = relationship("User", back_populates="student_profile")
    hostel_room = relationship("HostelRoom", back_populates="students", foreign_keys=[hostel_room_id])
    bus_route = relationship("BusRoute", back_populates="students", foreign_keys=[bus_route_id])


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    employee_code = Column(String(50), unique=True, index=True, nullable=True)
    department = Column(String(100), default="Computer Science")
    designation = Column(String(100), default="Assistant Professor")
    qualification = Column(String(150), default="M.Tech, Ph.D")
    experience_years = Column(Float, default=5.0)
    specialization = Column(String(200), default="Artificial Intelligence")
    phone_number = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    joining_date = Column(Date, default=datetime.date.today)

    user = relationship("User", back_populates="teacher_profile")
    # assignments via user


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    department = Column(String(100), default="Administration")
    access_level = Column(String(50), default="SUPER_ADMIN")

    user = relationship("User", back_populates="admin_profile")


class AdmissionStaff(Base):
    __tablename__ = "admission_staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    employee_id = Column(String(50), unique=True, nullable=True)

    user = relationship("User", back_populates="admission_profile")


class ExamStaff(Base):
    __tablename__ = "exam_staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    employee_id = Column(String(50), unique=True, nullable=True)

    user = relationship("User", back_populates="exam_profile")


class AccountStaff(Base):
    __tablename__ = "account_staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    employee_id = Column(String(50), unique=True, nullable=True)

    user = relationship("User", back_populates="account_profile")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(30), unique=True, index=True, nullable=False)
    name = Column(String(150), nullable=False)
    department = Column(String(100), nullable=False)
    semester = Column(Integer, default=1)
    credits = Column(Integer, default=3)
    hours_per_week = Column(Integer, default=4)
    syllabus = Column(Text, nullable=True)
    is_elective = Column(Boolean, default=False)

    timetable_entries = relationship("TimetableEntry", back_populates="subject", cascade="all, delete-orphan")
    attendances = relationship("Attendance", back_populates="subject", cascade="all, delete-orphan")
    marks = relationship("Mark", back_populates="subject", cascade="all, delete-orphan")
    assignments = relationship("Assignment", back_populates="subject", cascade="all, delete-orphan")
    modules = relationship("CourseModule", back_populates="subject", cascade="all, delete-orphan")


class TimetableEntry(Base):
    __tablename__ = "timetable_entries"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    section = Column(String(10), nullable=False)
    semester = Column(Integer, nullable=False)
    day_of_week = Column(String(20), nullable=False)
    hour_slot = Column(Integer, nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    room_number = Column(String(50), default="CR-101")

    subject = relationship("Subject", back_populates="timetable_entries")
    teacher = relationship("User")


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    date = Column(Date, default=datetime.date.today, index=True)
    hour_slot = Column(Integer, default=1)
    status = Column(String(20), default="Present")
    qr_code_hash = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    student_user = relationship("User", foreign_keys=[student_id], back_populates="attendances")
    subject = relationship("Subject", back_populates="attendances")


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    exam_type = Column(String(50), default="Mid-Term")
    semester = Column(Integer, default=1)
    academic_year = Column(String(20), default="2024-2025")
    department = Column(String(100), default="Computer Science")
    section = Column(String(10), default="A")
    marks_obtained = Column(Float, nullable=False)
    max_marks = Column(Float, default=100.0)
    grade = Column(String(5), default="A")
    remarks = Column(Text, nullable=True)
    status = Column(String(20), default="Published")

    student_user = relationship("User", foreign_keys=[student_id], back_populates="marks")
    subject = relationship("Subject", back_populates="marks")


class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    fee_type = Column(String(50), default="Tuition Fee")
    academic_year = Column(String(20), default="2024-2025")
    semester = Column(Integer, default=1)
    total_amount = Column(Numeric(10, 2), default=50000.00)
    paid_amount = Column(Numeric(10, 2), default=0.00)
    due_amount = Column(Numeric(10, 2), default=50000.00)
    due_date = Column(Date, default=datetime.date.today)
    status = Column(String(20), default="Pending")

    student_user = relationship("User", foreign_keys=[student_id], back_populates="fees")
    payments = relationship("FeePayment", back_populates="fee", cascade="all, delete-orphan")


class FeePayment(Base):
    __tablename__ = "fee_payments"

    id = Column(Integer, primary_key=True, index=True)
    fee_id = Column(Integer, ForeignKey("fees.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    payment_method = Column(String(50), default="Online UPI")
    transaction_id = Column(String(100), unique=True, nullable=True)
    receipt_number = Column(String(50), unique=True, nullable=True)
    status = Column(String(20), default="Completed")
    notes = Column(Text, nullable=True)

    fee = relationship("Fee", back_populates="payments")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    category = Column(String(50), default="General")
    priority = Column(String(20), default="Normal")
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", foreign_keys=[user_id], back_populates="notifications")


class Application(Base):
    __tablename__ = "applications"
    __table_args__ = (
        UniqueConstraint("email", "course_applied", name="uq_application_email_course"),
    )

    id = Column(Integer, primary_key=True, index=True)
    applicant_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(20), nullable=False)
    course_applied = Column(String(100), default="B.Tech Computer Science")
    tenth_percentage = Column(Float, default=85.0)
    twelfth_percentage = Column(Float, default=88.0)
    status = Column(String(20), default="Pending")
    submitted_at = Column(DateTime, default=datetime.datetime.utcnow)
    reviewed_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    review_notes = Column(Text, nullable=True)


class ExamHallTicket(Base):
    __tablename__ = "exam_hall_tickets"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    exam_name = Column(String(150), default="End Semester Theory Examinations")
    semester = Column(Integer, default=1)
    hall_ticket_number = Column(String(50), unique=True, index=True, nullable=False)
    issue_date = Column(Date, default=datetime.date.today)
    seat_number = Column(String(50), default="HALL-1-Seat-24")
    center_name = Column(String(150), default="Main Academic Block - Examination Wing")
    status = Column(String(20), default="Issued")

    student_user = relationship("User", foreign_keys=[student_id])


class CourseModule(Base):
    __tablename__ = "course_modules"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    module_number = Column(Integer, default=1)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    content_url = Column(String(255), nullable=True)
    resources_json = Column(Text, nullable=True)

    subject = relationship("Subject", back_populates="modules")


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    due_date = Column(DateTime, nullable=False)
    max_points = Column(Float, default=100.0)
    attachment_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    subject = relationship("Subject", back_populates="assignments")
    teacher = relationship("User", foreign_keys=[teacher_id])
    submissions = relationship("Submission", back_populates="assignment", cascade="all, delete-orphan")


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    submission_text = Column(Text, nullable=True)
    file_url = Column(String(255), nullable=True)
    submitted_at = Column(DateTime, default=datetime.datetime.utcnow)
    marks_awarded = Column(Float, nullable=True)
    feedback = Column(Text, nullable=True)
    status = Column(String(20), default="Submitted")

    assignment = relationship("Assignment", back_populates="submissions")
    student_user = relationship("User", foreign_keys=[student_id])


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String(50), unique=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    author = Column(String(200), nullable=False)
    publisher = Column(String(150), default="Pearson")
    category = Column(String(100), default="Computer Science")
    total_copies = Column(Integer, default=5)
    available_copies = Column(Integer, default=5)
    rack_location = Column(String(50), default="Shelf B-04")
    cover_image = Column(String(255), nullable=True)
    publication_year = Column(Integer, default=2023)

    borrows = relationship("BookBorrow", back_populates="book", cascade="all, delete-orphan")


class BookBorrow(Base):
    __tablename__ = "book_borrows"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    borrow_date = Column(Date, default=datetime.date.today)
    due_date = Column(Date, default=lambda: datetime.date.today() + datetime.timedelta(days=14))
    return_date = Column(Date, nullable=True)
    fine_amount = Column(Numeric(8, 2), default=0.00)
    status = Column(String(20), default="Issued")

    book = relationship("Book", back_populates="borrows")
    user = relationship("User", back_populates="book_borrows")


class Hostel(Base):
    __tablename__ = "hostels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(20), default="Boys")
    warden_name = Column(String(100), default="Dr. John Smith")
    warden_phone = Column(String(20), default="+91 9876543210")
    total_rooms = Column(Integer, default=100)
    address = Column(Text, default="Campus North Wing")

    rooms = relationship("HostelRoom", back_populates="hostel", cascade="all, delete-orphan")


class HostelRoom(Base):
    __tablename__ = "hostel_rooms"

    id = Column(Integer, primary_key=True, index=True)
    hostel_id = Column(Integer, ForeignKey("hostels.id", ondelete="CASCADE"), nullable=False)
    room_number = Column(String(20), nullable=False)
    floor = Column(Integer, default=1)
    capacity = Column(Integer, default=2)
    occupied_count = Column(Integer, default=0)
    rent_per_semester = Column(Numeric(10, 2), default=35000.00)
    amenities = Column(String(255), default="Attached Bath, Wi-Fi, AC")

    hostel = relationship("Hostel", back_populates="rooms")
    students = relationship("Student", back_populates="hostel_room", foreign_keys="Student.hostel_room_id")


class BusRoute(Base):
    __tablename__ = "bus_routes"

    id = Column(Integer, primary_key=True, index=True)
    route_number = Column(String(30), unique=True, nullable=False)
    route_name = Column(String(150), nullable=False)
    start_point = Column(String(100), nullable=False)
    end_point = Column(String(100), default="Collexa Main Campus")
    driver_name = Column(String(100), default="Mr. Ramesh Kumar")
    driver_phone = Column(String(20), default="+91 9123456780")
    bus_number = Column(String(30), default="DL-01-AB-1234")
    capacity = Column(Integer, default=50)
    stops_json = Column(Text, default="[]")
    departure_time = Column(String(20), default="07:30 AM")

    students = relationship("Student", back_populates="bus_route", foreign_keys="Student.bus_route_id")
    passes = relationship("TransportPass", back_populates="route")


class TransportPass(Base):
    __tablename__ = "transport_passes"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    route_id = Column(Integer, ForeignKey("bus_routes.id", ondelete="CASCADE"), nullable=False)
    pass_number = Column(String(50), unique=True, index=True, nullable=False)
    valid_from = Column(Date, default=datetime.date.today)
    valid_until = Column(Date, default=lambda: datetime.date.today() + datetime.timedelta(days=180))
    amount_paid = Column(Numeric(10, 2), default=12000.00)
    status = Column(String(20), default="Active")

    student_user = relationship("User", foreign_keys=[student_id])
    route = relationship("BusRoute", back_populates="passes")


class JobDrive(Base):
    __tablename__ = "job_drives"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(150), nullable=False)
    job_title = Column(String(150), nullable=False)
    job_description = Column(Text, nullable=False)
    eligibility_cgpa = Column(Float, default=7.0)
    eligible_departments = Column(String(255), default="Computer Science, IT")
    salary_package = Column(String(50), default="12 LPA")
    drive_date = Column(Date, default=lambda: datetime.date.today() + datetime.timedelta(days=15))
    registration_deadline = Column(Date, default=lambda: datetime.date.today() + datetime.timedelta(days=10))
    location = Column(String(100), default="Bangalore / Remote")
    status = Column(String(20), default="Active")

    applications = relationship("JobApplication", back_populates="drive", cascade="all, delete-orphan")


class JobApplication(Base):
    __tablename__ = "job_applications"
    __table_args__ = (
        UniqueConstraint("drive_id", "student_id", name="uq_job_app_drive_student"),
    )

    id = Column(Integer, primary_key=True, index=True)
    drive_id = Column(Integer, ForeignKey("job_drives.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    applied_at = Column(DateTime, default=datetime.datetime.utcnow)
    resume_url = Column(String(255), default="https://example.com/resume.pdf")
    status = Column(String(30), default="Applied")
    feedback = Column(Text, nullable=True)

    drive = relationship("JobDrive", back_populates="applications")
    student_user = relationship("User", foreign_keys=[student_id])


class CampusEvent(Base):
    __tablename__ = "campus_events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), default="Technical")
    organizer = Column(String(100), default="Coding Club")
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, default=lambda: datetime.datetime.utcnow() + datetime.timedelta(hours=4))
    venue = Column(String(150), default="Auditorium")
    banner_url = Column(String(255), nullable=True)
    registration_fee = Column(Numeric(8, 2), default=0.00)
    max_participants = Column(Integer, default=200)

    registrations = relationship("EventRegistration", back_populates="event", cascade="all, delete-orphan")


class EventRegistration(Base):
    __tablename__ = "event_registrations"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("campus_events.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)
    ticket_code = Column(String(50), unique=True, index=True, nullable=False)
    payment_status = Column(String(20), default="Free")
    attendance_status = Column(String(20), default="Registered")

    event = relationship("CampusEvent", back_populates="registrations")
    user = relationship("User")


class ChatChannel(Base):
    __tablename__ = "chat_channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    is_private = Column(Boolean, default=False)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    messages = relationship("ChatMessage", back_populates="channel", cascade="all, delete-orphan")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(Integer, ForeignKey("chat_channels.id", ondelete="CASCADE"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    attachment_url = Column(String(255), nullable=True)
    sent_at = Column(DateTime, default=datetime.datetime.utcnow)

    channel = relationship("ChatChannel", back_populates="messages")
    sender = relationship("User", back_populates="sent_messages")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    action = Column(String(100), nullable=False)
    entity = Column(String(50), nullable=False)
    entity_id = Column(String(50), nullable=True)
    details = Column(Text, nullable=True)
    ip_address = Column(String(50), default="127.0.0.1")
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="audit_logs")


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    faculty_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="SET NULL"), nullable=True)
    rating = Column(Integer, default=5)
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Grievance(Base):
    __tablename__ = "grievances"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(100), default="Academic")
    status = Column(String(50), default="Pending")
    resolution_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class AdmissionRequest(Base):
    __tablename__ = "admission_requests"
    __table_args__ = (
        UniqueConstraint("email", "desired_course", name="uq_admission_request_email_course"),
    )

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    phone_number = Column(String(20), nullable=False)
    desired_course = Column(String(100), default="Computer Science")
    status = Column(String(50), default="Pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class SystemConfig(Base):
    __tablename__ = "system_configs"

    id = Column(Integer, primary_key=True, index=True)
    mark_entry_enabled = Column(Boolean, default=True)
    results_published = Column(Boolean, default=False)

class QuestionPaper(Base):
    __tablename__ = "question_papers"

    id = Column(Integer, primary_key=True, index=True)
    subject_code = Column(String(50), nullable=False)
    subject_name = Column(String(150), nullable=False)
    semester = Column(Integer, default=1)
    exam_type = Column(String(50), default="End-Term")
    file_url = Column(String(255), default="https://collexa.edu/papers/sample.pdf")
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
