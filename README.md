# Collexa Enterprise Campus Management System & Academic LMS

Collexa is an enterprise-grade, full-stack Higher Education Institution ERP, Academic Learning Management System (LMS), and Examination Operations Platform.

Designed for universities and autonomous colleges, Collexa unifies student lifecycles, faculty workflows, attendance tracking, examination proctoring, corporate placements, hostel & transport fleets, financial payroll, and institutional BI telemetry into a high-performance system.

---

## 🏛️ System Architecture & Key Modules

1. **Academic & Learning Management System (LMS)**: Course syllabi, module lecture notes, assignment submission pipelines, and grading workflows.
2. **Timetable Matrix Engine**: Conflict-free 6-period timetable scheduler across classrooms, departments, and faculty.
3. **Examination Cell & AI Proctoring**: Mid-term/semester exams with tab-switch logging, face visibility detection, marks moderation, and hall ticket issuance.
4. **Digitally Signed Certificates**: SHA-256 tamper-proof bonafide certificates and transcripts.
5. **Central Digital Library**: 25,000+ title catalog, 14-day circulation, overdue fine calculations, and rack locator.
6. **Corporate Placement & Careers**: Tier-1 recruitment drives, CGPA eligibility engine, resume submission, and candidate tracking.
7. **Hostel & Transport Fleet**: Residential hall blocks, mess schedules, shuttle bus transit routes, and driver contacts.
8. **Financial Management & Payroll**: Fee challan invoicing, payment ledgers, and staff/faculty salary slips with HRA, DA, PF, and TDS breakdowns.
9. **Asset & Lab Inventory**: Laboratory equipment lifecycle tracking and depreciation auditing.
10. **Alumni Mentorship Network**: Global alumni directory with mentorship status and connections.
11. **Grievance Redressal Desk**: Student and staff ticketing with 48hr SLA resolution tracking.
12. **AI Campus Knowledge Advisor**: Natural language institutional advisor and heuristic academic risk predictor.
13. **Real-Time Collaboration**: WebSocket channels and study group chat.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.11+ / 3.14, FastAPI, SQLAlchemy 2.0, Pydantic V2, Uvicorn, Bcrypt, PyJWT, PyTest.
- **Frontend**: React 18, Vite, Tailwind CSS, Lucide React icons, Axios, React Router 6.
- **Database**: SQLite / PostgreSQL compatible SQLAlchemy ORM.
- **Real-Time**: WebSockets for channel messaging and live notifications.

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+ (with `pip`)
- Node.js 18+ (with `npm`)

### 1. Clone the Repository
```bash
git clone https://github.com/gandhikomarala/Coding-Raja-Internship.git
cd Collexa
```

### 2. Environment Configuration
Copy the example environment files:
```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### 3. Install Dependencies

**Backend:**
```bash
cd backend
python -m venv myenv
# Windows:
.\myenv\Scripts\activate
# Linux/macOS:
source myenv/bin/activate

pip install -r requirements.txt
cd ..
```

**Frontend:**
```bash
cd frontend
npm install
cd ..
```

---

## 💻 Running the Application

### Option A: Direct Python Runner (Recommended)
From the project root directory, run:
```bash
python run.py
```
This automatically seeds demo data and launches both the backend (`http://127.0.0.1:8000`) and frontend (`http://127.0.0.1:5173`).

### Option B: Manual Service Launch

**1. Launch Backend Server:**
```bash
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

**2. Launch Frontend Dev Server:**
```bash
cd frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

### Option C: Docker & Docker Compose
```bash
docker compose up --build
```

---

## 🧪 Testing Suite

Run the full automated test suite with `pytest`:
```bash
pytest backend/tests
```

To run with verbose output:
```bash
pytest backend/tests -v
```

---

## 🔑 Demo User Credentials

The system includes pre-seeded accounts for testing all institutional workflows:

| Role | Email | Password | Primary Capabilities |
| :--- | :--- | :--- | :--- |
| **Super Admin** | `admin@collexa.edu` | `admin123` | Master configuration, Executive BI, Timetable, Payroll, Asset Inventory |
| **Faculty / Teacher** | `teacher@collexa.edu` | `teacher123` | Faculty Hub, LMS Gradebook, QR Attendance, Timetable Matrix, Salary Slips |
| **Student** | `student@collexa.edu` | `student123` | Student Hub, LMS, Online Exams, Library, Placements, ID Pass, AI Advisor |
| **Accounts / Finance** | `account@collexa.edu` | `account123` | Fee Invoicing, Receipts, Financial Ledgers, Payroll Disbursal |
| **Exam Cell** | `exam@collexa.edu` | `exam123` | Hall Tickets, Marks Moderation, Results Publishing |
| **Admissions** | `admission@collexa.edu` | `admission123` | Student Applications, Auto-Onboarding |

---

## 📖 API Documentation

Once the backend is running, interactive API documentation is available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📁 Project Directory Structure

```
Collexa/
├── backend/
│   ├── core/                  # Core security, caching, logging, auditing
│   ├── engines/               # Scheduling, Proctoring, Payroll, Inventory, Certificates
│   ├── routers/               # 16+ API domain controllers
│   ├── services/              # Business logic services (GPA, Fees, Attendance, etc.)
│   ├── seeders/               # University catalogs and mock datasets
│   ├── tests/                 # PyTest test suite
│   ├── database.py            # Database connection & SQLite sessionmaker
│   ├── models.py              # 30+ Relational SQLAlchemy ORM models
│   ├── schemas.py             # Pydantic V2 validation schemas
│   ├── auth.py                # Bcrypt & JWT security layer
│   ├── dependencies.py        # RBAC role checkers and auth dependencies
│   ├── websocket_manager.py   # Connection pooling and live broadcasts
│   └── main.py                # FastAPI main application
│
├── frontend/
│   ├── src/
│   │   ├── pages/             # 20+ Full-stack institutional portals & dashboards
│   │   ├── components/        # Reusable UI component design system
│   │   ├── constants/         # Curriculum, departments, and calendar datasets
│   │   ├── context/           # React AuthContext
│   │   ├── layouts/           # MainLayout sidebar navigation
│   │   ├── services/          # Axios API communication client
│   │   ├── App.jsx            # Role-protected routing system
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
│
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── run.py                     # Root executable orchestrator
└── README.md                  # System documentation
```
