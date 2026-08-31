from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, database, auth, dependencies

router = APIRouter()

@router.post("/register", response_model=schemas.UserDetailed)
async def register(user_in: schemas.UserCreateExtended, db: Session = Depends(database.get_db)):
    existing = db.query(models.User).filter(models.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="An account with this email already exists.")
    
    db_user = models.User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=auth.get_password_hash(user_in.password),
        role=user_in.role,
        phone_number=user_in.phone_number,
        avatar_url=user_in.avatar_url,
        is_active=True
    )
    db.add(db_user)
    db.flush()

    if user_in.role == models.UserRole.STUDENT:
        student = models.Student(
            user_id=db_user.id,
            roll_number=user_in.roll_number or f"COL24CS{db_user.id:03d}",
            department=user_in.department or "Computer Science",
            year=user_in.year or 1,
            section=user_in.section or "A",
            batch=user_in.batch or "2023-2027"
        )
        db.add(student)
    elif user_in.role == models.UserRole.TEACHER:
        teacher = models.Teacher(
            user_id=db_user.id,
            employee_code=user_in.employee_code or f"EMP{db_user.id:04d}",
            department=user_in.department or "Computer Science",
            designation=user_in.designation or "Assistant Professor"
        )
        db.add(teacher)
    elif user_in.role == models.UserRole.ADMIN:
        admin = models.Admin(user_id=db_user.id, department="Administration", access_level="SUPER_ADMIN")
        db.add(admin)
    elif user_in.role == models.UserRole.ADMISSION:
        admission = models.AdmissionStaff(user_id=db_user.id, employee_id=f"ADM{db_user.id:03d}")
        db.add(admission)
    elif user_in.role == models.UserRole.EXAM:
        exam = models.ExamStaff(user_id=db_user.id, employee_id=f"EXM{db_user.id:03d}")
        db.add(exam)
    elif user_in.role == models.UserRole.ACCOUNT:
        acc = models.AccountStaff(user_id=db_user.id, employee_id=f"ACC{db_user.id:03d}")
        db.add(acc)

    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=schemas.Token)
async def login(credentials: schemas.LoginRequest, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.email).first()
    if not user or not auth.verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Account is deactivated")

    access_token = auth.create_access_token(
        data={"sub": user.email, "email": user.email, "role": user.role.value if hasattr(user.role, 'value') else str(user.role), "user_id": user.id}
    )
    
    user_data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role.value if hasattr(user.role, 'value') else str(user.role),
        "phone_number": user.phone_number,
        "avatar_url": user.avatar_url
    }

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user_data
    }

@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Account is deactivated")

    access_token = auth.create_access_token(
        data={"sub": user.email, "email": user.email, "role": user.role.value if hasattr(user.role, 'value') else str(user.role), "user_id": user.id}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role.value if hasattr(user.role, 'value') else str(user.role)
    }

@router.get("/me", response_model=schemas.UserDetailed)
async def get_me(current_user: models.User = Depends(dependencies.get_current_user)):
    return current_user
