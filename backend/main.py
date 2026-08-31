from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, get_db
from websocket_manager import manager
from routers import (
    auth, admin, student, teacher, staff, timetable, ai,
    courses, exams, finance, library, placements, hostel_transport,
    events, chat, analytics, proctoring, payroll, inventory, alumni,
    scholarships, certificates, grievances
)

# Auto-create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Collexa Enterprise Campus Management System",
    description="End-to-End Higher Education ERP, LMS, Examination, Finance & Campus Operations API",
    version="2.5.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fast OAuth2 token endpoint
@app.post("/token")
async def root_token(form_data: auth.OAuth2PasswordRequestForm = Depends(), db: auth.Session = Depends(get_db)):
    return await auth.login_for_access_token(form_data, db)

# Include Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication & Access Control"])
app.include_router(admin.router, prefix="/api/admin", tags=["Super Admin & User Management"])
app.include_router(student.router, prefix="/api/student", tags=["Student Lifecycle & Self-Service"])
app.include_router(teacher.router, prefix="/api/teacher", tags=["Faculty Management & Grading"])
app.include_router(staff.router, prefix="/api/staff", tags=["Staff Operations & Admissions"])
app.include_router(timetable.router, prefix="/api/timetable", tags=["Timetable & Scheduling"])
app.include_router(courses.router, prefix="/api/courses", tags=["Academic LMS & Course Modules"])
app.include_router(exams.router, prefix="/api/exams", tags=["Examination & Transcripts"])
app.include_router(finance.router, prefix="/api/finance", tags=["Accounts & Fee Invoicing"])
app.include_router(library.router, prefix="/api/library", tags=["Library Management System"])
app.include_router(placements.router, prefix="/api/placements", tags=["Placement & Career Center"])
app.include_router(hostel_transport.router, prefix="/api/hostel-transport", tags=["Hostel & Fleet Transport"])
app.include_router(events.router, prefix="/api/events", tags=["Campus Events & Clubs"])
app.include_router(chat.router, prefix="/api/chat", tags=["Campus Realtime Chat & Channels"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Executive BI & Analytics"])
app.include_router(proctoring.router, prefix="/api/proctoring", tags=["Online Exam Proctoring"])
app.include_router(payroll.router, prefix="/api/payroll", tags=["Payroll & Salary Slips"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["Campus Asset Inventory"])
app.include_router(alumni.router, prefix="/api/alumni", tags=["Alumni Network & Directory"])
app.include_router(scholarships.router, prefix="/api/scholarships", tags=["Scholarships & Grants"])
app.include_router(certificates.router, prefix="/api/certificates", tags=["Certificates & Transcripts"])
app.include_router(grievances.router, prefix="/api/grievances", tags=["Grievance Redressal"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI Academic Assistant"])

# WebSocket Endpoint for Realtime Notifications & Attendance Sessions
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Echo or broadcast message
            await manager.broadcast({"type": "MESSAGE", "data": data})
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# WebSocket Endpoint for Specific Chat Channels
@app.websocket("/ws/channel/{channel_id}")
async def channel_websocket(websocket: WebSocket, channel_id: int):
    await websocket.accept()
    manager.subscribe_channel(channel_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast_to_channel(channel_id, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/")
async def root():
    return {
        "status": "Online",
        "app": "Collexa Enterprise Campus Management ERP",
        "version": "2.5.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "database": "connected"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
