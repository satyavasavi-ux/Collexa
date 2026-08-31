from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Optional, Any
from datetime import datetime, date
from decimal import Decimal
from models import UserRole

# ==========================================
# AUTH & TOKEN SCHEMAS
# ==========================================
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Optional[Any] = None

class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None

class LoginRequest(BaseModel):
    email: str
    password: str

# ==========================================
# USER & PROFILES SCHEMAS
# ==========================================
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole = UserRole.STUDENT
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserCreateExtended(UserCreate):
    roll_number: Optional[str] = None
    department: Optional[str] = None
    year: Optional[int] = None
    section: Optional[str] = None
    batch: Optional[str] = None
    employee_code: Optional[str] = None
    designation: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    is_active: Optional[bool] = None

class StudentProfile(BaseModel):
    id: int
    user_id: int
    roll_number: Optional[str] = None
    department: Optional[str] = "Computer Science"
    year: Optional[int] = 1
    semester: Optional[int] = 1
    section: Optional[str] = "A"
    batch: Optional[str] = "2023-2027"
    phone_number: Optional[str] = None
    address: Optional[str] = None
    guardian_name: Optional[str] = None
    guardian_phone: Optional[str] = None
    blood_group: Optional[str] = None
    dob: Optional[date] = None
    cgpa: Optional[float] = 0.0
    credits_completed: Optional[int] = 0
    model_config = ConfigDict(from_attributes=True)

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    guardian_name: Optional[str] = None
    guardian_phone: Optional[str] = None

class TeacherProfile(BaseModel):
    id: int
    user_id: int
    employee_code: Optional[str] = None
    department: Optional[str] = "Computer Science"
    designation: Optional[str] = "Assistant Professor"
    qualification: Optional[str] = "Ph.D"
    experience_years: Optional[float] = 5.0
    specialization: Optional[str] = "Artificial Intelligence"
    phone_number: Optional[str] = None
    address: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    qualification: Optional[str] = None
    specialization: Optional[str] = None

class AdminStaff(BaseModel):
    id: int
    user_id: int
    department: str
    access_level: str
    model_config = ConfigDict(from_attributes=True)

class AdmissionStaff(BaseModel):
    id: int
    user_id: int
    employee_id: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class ExamStaff(BaseModel):
    id: int
    user_id: int
    employee_id: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class AccountStaff(BaseModel):
    id: int
    user_id: int
    employee_id: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    student_profile: Optional[StudentProfile] = None
    teacher_profile: Optional[TeacherProfile] = None
    model_config = ConfigDict(from_attributes=True)

class UserDetailed(User):
    admin_profile: Optional[AdminStaff] = None
    admission_profile: Optional[AdmissionStaff] = None
    exam_profile: Optional[ExamStaff] = None
    account_profile: Optional[AccountStaff] = None
    model_config = ConfigDict(from_attributes=True)

class StudentWithAttendance(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole
    created_at: datetime
    attendance_percentage: float
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# SUBJECT & TIMETABLE SCHEMAS
# ==========================================
class SubjectBase(BaseModel):
    code: str
    name: str
    department: str
    semester: int = 1
    credits: int = 3
    hours_per_week: int = 4
    syllabus: Optional[str] = None
    is_elective: bool = False

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TimetableEntryBase(BaseModel):
    department: str
    year: int
    section: str
    semester: int
    day_of_week: str
    hour_slot: int
    subject_id: int
    teacher_id: int
    room_number: Optional[str] = "CR-101"

class TimetableEntryCreate(TimetableEntryBase):
    pass

class TimetableEntry(TimetableEntryBase):
    id: int
    subject: Optional[Subject] = None
    teacher: Optional[User] = None
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# ATTENDANCE SCHEMAS
# ==========================================
class AttendanceSessionStart(BaseModel):
    subject_id: int
    hour_slot: int
    department: Optional[str] = None
    section: Optional[str] = None

class AttendanceBase(BaseModel):
    student_id: int
    subject_id: int
    date: date
    hour_slot: int = 1
    status: str = "Present"

class AttendanceCreate(AttendanceBase):
    teacher_id: Optional[int] = None
    qr_code_hash: Optional[str] = None

class Attendance(AttendanceBase):
    id: int
    teacher_id: Optional[int] = None
    created_at: datetime
    subject: Optional[Subject] = None
    model_config = ConfigDict(from_attributes=True)

class AttendanceStats(BaseModel):
    total_classes: int
    attended_classes: int
    percentage: float

# ==========================================
# MARKS & EXAMS SCHEMAS
# ==========================================
class MarkBase(BaseModel):
    student_id: int
    subject_id: int
    exam_type: str = "Mid-Term"
    semester: int = 1
    marks_obtained: float
    max_marks: float = 100.0
    grade: str = "A"
    remarks: Optional[str] = None
    status: str = "Published"

class MarkCreate(MarkBase):
    teacher_id: Optional[int] = None

class Mark(MarkBase):
    id: int
    teacher_id: Optional[int] = None
    subject: Optional[Subject] = None
    model_config = ConfigDict(from_attributes=True)

class ExamHallTicketBase(BaseModel):
    student_id: int
    exam_name: str = "End Semester Examinations"
    semester: int = 1
    hall_ticket_number: str
    issue_date: date = Field(default_factory=date.today)
    seat_number: str = "Seat-01"
    center_name: str = "Examination Wing"
    status: str = "Issued"

class ExamHallTicketCreate(ExamHallTicketBase):
    pass

class ExamHallTicket(ExamHallTicketBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# FEES & ACCOUNTS SCHEMAS
# ==========================================
class FeeBase(BaseModel):
    student_id: int
    fee_type: str = "Tuition Fee"
    academic_year: str = "2024-2025"
    semester: int = 1
    total_amount: Decimal = Decimal("50000.00")
    paid_amount: Decimal = Decimal("0.00")
    due_amount: Decimal = Decimal("50000.00")
    due_date: date = Field(default_factory=date.today)
    status: str = "Pending"

class FeeCreate(FeeBase):
    pass

class FeePaymentBase(BaseModel):
    fee_id: int
    amount: Decimal
    payment_method: str = "Online UPI"
    transaction_id: Optional[str] = None
    receipt_number: Optional[str] = None
    status: str = "Completed"
    notes: Optional[str] = None

class FeePaymentCreate(FeePaymentBase):
    pass

class FeePayment(FeePaymentBase):
    id: int
    payment_date: datetime
    model_config = ConfigDict(from_attributes=True)

class Fee(FeeBase):
    id: int
    payments: List[FeePayment] = []
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# NOTIFICATIONS SCHEMAS
# ==========================================
class NotificationBase(BaseModel):
    student_id: Optional[int] = None
    user_id: Optional[int] = None
    title: str
    message: str
    category: str = "General"
    priority: str = "Normal"
    is_read: bool = False

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# ADMISSIONS SCHEMAS
# ==========================================
class ApplicationBase(BaseModel):
    applicant_name: str
    email: EmailStr
    phone: str
    course_applied: str = "B.Tech Computer Science"
    tenth_percentage: float = 85.0
    twelfth_percentage: float = 88.0
    status: str = "Pending"
    review_notes: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int
    submitted_at: datetime
    reviewed_by: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# COURSE LMS & ASSIGNMENTS SCHEMAS
# ==========================================
class CourseModuleBase(BaseModel):
    subject_id: int
    module_number: int = 1
    title: str
    description: Optional[str] = None
    content_url: Optional[str] = None
    resources_json: Optional[str] = None

class CourseModuleCreate(CourseModuleBase):
    pass

class CourseModule(CourseModuleBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class AssignmentBase(BaseModel):
    subject_id: int
    title: str
    description: str
    due_date: datetime
    max_points: float = 100.0
    attachment_url: Optional[str] = None

class AssignmentCreate(AssignmentBase):
    teacher_id: Optional[int] = None

class SubmissionBase(BaseModel):
    assignment_id: int
    student_id: int
    submission_text: Optional[str] = None
    file_url: Optional[str] = None

class SubmissionCreate(SubmissionBase):
    pass

class SubmissionGrade(BaseModel):
    marks_awarded: float
    feedback: Optional[str] = None

class Submission(SubmissionBase):
    id: int
    submitted_at: datetime
    marks_awarded: Optional[float] = None
    feedback: Optional[str] = None
    status: str = "Submitted"
    model_config = ConfigDict(from_attributes=True)

class Assignment(AssignmentBase):
    id: int
    teacher_id: int
    created_at: datetime
    subject: Optional[Subject] = None
    submissions: List[Submission] = []
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# LIBRARY SCHEMAS
# ==========================================
class BookBase(BaseModel):
    isbn: str
    title: str
    author: str
    publisher: Optional[str] = "Pearson"
    category: Optional[str] = "Computer Science"
    total_copies: int = 5
    available_copies: int = 5
    rack_location: Optional[str] = "Shelf B-04"
    cover_image: Optional[str] = None
    publication_year: Optional[int] = 2023

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookBorrowBase(BaseModel):
    book_id: int
    user_id: int
    borrow_date: date = Field(default_factory=date.today)
    due_date: Optional[date] = None
    status: str = "Issued"

class BookBorrowCreate(BookBorrowBase):
    pass

class BookBorrow(BookBorrowBase):
    id: int
    return_date: Optional[date] = None
    fine_amount: Decimal = Decimal("0.00")
    book: Optional[Book] = None
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# HOSTEL & TRANSPORT SCHEMAS
# ==========================================
class HostelRoomBase(BaseModel):
    hostel_id: int
    room_number: str
    floor: int = 1
    capacity: int = 2
    occupied_count: int = 0
    rent_per_semester: Decimal = Decimal("35000.00")
    amenities: Optional[str] = "Attached Bath, Wi-Fi, AC"

class HostelRoomCreate(HostelRoomBase):
    pass

class HostelRoom(HostelRoomBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class HostelBase(BaseModel):
    name: str
    type: str = "Boys"
    warden_name: str = "Dr. John Smith"
    warden_phone: str = "+91 9876543210"
    total_rooms: int = 100
    address: str = "Campus North Wing"

class HostelCreate(HostelBase):
    pass

class Hostel(HostelBase):
    id: int
    rooms: List[HostelRoom] = []
    model_config = ConfigDict(from_attributes=True)

class BusRouteBase(BaseModel):
    route_number: str
    route_name: str
    start_point: str
    end_point: str = "Collexa Main Campus"
    driver_name: str = "Mr. Ramesh Kumar"
    driver_phone: str = "+91 9123456780"
    bus_number: str = "DL-01-AB-1234"
    capacity: int = 50
    stops_json: str = "[]"
    departure_time: str = "07:30 AM"

class BusRouteCreate(BusRouteBase):
    pass

class BusRoute(BusRouteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TransportPassBase(BaseModel):
    student_id: int
    route_id: int
    pass_number: str
    valid_from: date = Field(default_factory=date.today)
    valid_until: Optional[date] = None
    amount_paid: Decimal = Decimal("12000.00")
    status: str = "Active"

class TransportPassCreate(TransportPassBase):
    pass

class TransportPass(TransportPassBase):
    id: int
    route: Optional[BusRoute] = None
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# PLACEMENTS SCHEMAS
# ==========================================
class JobDriveBase(BaseModel):
    company_name: str
    job_title: str
    job_description: str
    eligibility_cgpa: float = 7.0
    eligible_departments: str = "Computer Science, IT"
    salary_package: str = "12 LPA"
    drive_date: date
    registration_deadline: date
    location: str = "Bangalore / Remote"
    status: str = "Active"

class JobDriveCreate(JobDriveBase):
    pass

class JobApplicationBase(BaseModel):
    drive_id: int
    student_id: int
    resume_url: str = "https://example.com/resume.pdf"
    status: str = "Applied"
    feedback: Optional[str] = None

class JobApplicationCreate(JobApplicationBase):
    pass

class JobApplication(JobApplicationBase):
    id: int
    applied_at: datetime
    drive: Optional[JobDriveBase] = None
    model_config = ConfigDict(from_attributes=True)

class JobDrive(JobDriveBase):
    id: int
    applications: List[JobApplication] = []
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# EVENTS & CLUBS SCHEMAS
# ==========================================
class CampusEventBase(BaseModel):
    title: str
    description: str
    category: str = "Technical"
    organizer: str = "Coding Club"
    start_time: datetime
    end_time: datetime
    venue: str = "Auditorium"
    banner_url: Optional[str] = None
    registration_fee: Decimal = Decimal("0.00")
    max_participants: int = 200

class CampusEventCreate(CampusEventBase):
    pass

class EventRegistrationBase(BaseModel):
    event_id: int
    user_id: int
    ticket_code: str
    payment_status: str = "Free"
    attendance_status: str = "Registered"

class EventRegistrationCreate(EventRegistrationBase):
    pass

class EventRegistration(EventRegistrationBase):
    id: int
    registered_at: datetime
    event: Optional[CampusEventBase] = None
    model_config = ConfigDict(from_attributes=True)

class CampusEvent(CampusEventBase):
    id: int
    registrations: List[EventRegistration] = []
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# REALTIME CHAT SCHEMAS
# ==========================================
class ChatChannelBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_private: bool = False

class ChatChannelCreate(ChatChannelBase):
    pass

class ChatMessageBase(BaseModel):
    channel_id: int
    content: str
    attachment_url: Optional[str] = None

class ChatMessageCreate(ChatMessageBase):
    sender_id: Optional[int] = None

class ChatMessage(ChatMessageBase):
    id: int
    sender_id: int
    sent_at: datetime
    sender: Optional[UserBase] = None
    model_config = ConfigDict(from_attributes=True)

class ChatChannel(ChatChannelBase):
    id: int
    created_by: Optional[int] = None
    created_at: datetime
    messages: List[ChatMessage] = []
    model_config = ConfigDict(from_attributes=True)

# ==========================================
# AUDIT LOG SCHEMAS
# ==========================================
class AuditLogBase(BaseModel):
    user_id: Optional[int] = None
    action: str
    entity: str
    entity_id: Optional[str] = None
    details: Optional[str] = None
    ip_address: Optional[str] = "127.0.0.1"

class AuditLog(AuditLogBase):
    id: int
    timestamp: datetime
    user: Optional[UserBase] = None
    model_config = ConfigDict(from_attributes=True)


class FeedbackBase(BaseModel):
    faculty_id: Optional[int] = None
    subject_id: Optional[int] = None
    rating: int = 5
    comments: Optional[str] = None

class Feedback(FeedbackBase):
    id: int
    student_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class GrievanceCreate(BaseModel):
    title: str
    description: str
    category: str = "Academic"

class Grievance(GrievanceCreate):
    id: int
    student_id: int
    status: str = "Pending"
    resolution_notes: Optional[str] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class AttendanceMarkRequest(BaseModel):
    qr_code_data: str

class AdmissionRequestBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    desired_course: str = "Computer Science"
    status: str = "Pending"

class AdmissionRequest(AdmissionRequestBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class SystemConfig(BaseModel):
    id: int
    mark_entry_enabled: bool = True
    results_published: bool = False
    model_config = ConfigDict(from_attributes=True)

class QuestionPaperCreate(BaseModel):
    subject_code: str
    subject_name: str
    semester: int
    exam_type: str
    file_url: Optional[str] = None

class QuestionPaper(BaseModel):
    id: int
    subject_code: str
    subject_name: str
    semester: int
    exam_type: str
    file_url: str
    uploaded_at: datetime
    model_config = ConfigDict(from_attributes=True)
