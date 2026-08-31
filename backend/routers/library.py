from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal
import datetime
import models, schemas, database, dependencies

router = APIRouter()

@router.get("/books", response_model=List[schemas.Book])
async def list_books(
    search: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.Book)
    if search:
        query = query.filter((models.Book.title.ilike(f"%{search}%")) | (models.Book.author.ilike(f"%{search}%")) | (models.Book.isbn.ilike(f"%{search}%")))
    if category:
        query = query.filter(models.Book.category == category)
    return query.all()

@router.post("/books", response_model=schemas.Book)
async def add_book(
    book_in: schemas.BookCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["LIBRARY", "ADMIN"]))
):
    existing = db.query(models.Book).filter(models.Book.isbn == book_in.isbn).first()
    if existing:
        raise HTTPException(status_code=400, detail="A book with this ISBN already exists")
    book = models.Book(**book_in.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.post("/issue", response_model=schemas.BookBorrow)
async def issue_book(
    borrow_in: schemas.BookBorrowCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["LIBRARY", "ADMIN"]))
):
    book = db.query(models.Book).filter(models.Book.id == borrow_in.book_id).first()
    if not book or book.available_copies <= 0:
        raise HTTPException(status_code=400, detail="Book is not available for issue")

    user = db.query(models.User).filter(models.User.id == borrow_in.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    due = borrow_in.due_date or (datetime.date.today() + datetime.timedelta(days=14))
    borrow = models.BookBorrow(
        book_id=borrow_in.book_id,
        user_id=borrow_in.user_id,
        borrow_date=borrow_in.borrow_date,
        due_date=due,
        status="Issued"
    )
    book.available_copies -= 1
    db.add(borrow)
    db.commit()
    db.refresh(borrow)
    return borrow

@router.post("/return/{borrow_id}", response_model=schemas.BookBorrow)
async def return_book(
    borrow_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["LIBRARY", "ADMIN"]))
):
    borrow = db.query(models.BookBorrow).filter(models.BookBorrow.id == borrow_id).first()
    if not borrow or borrow.status == "Returned":
        raise HTTPException(status_code=400, detail="Invalid borrow record")

    today = datetime.date.today()
    borrow.return_date = today
    borrow.status = "Returned"

    if borrow.due_date and today > borrow.due_date:
        days_over = (today - borrow.due_date).days
        borrow.fine_amount = Decimal(str(days_over * 10))

    book = db.query(models.Book).filter(models.Book.id == borrow.book_id).first()
    if book:
        book.available_copies += 1

    db.commit()
    db.refresh(borrow)
    return borrow

@router.get("/borrows/active", response_model=List[schemas.BookBorrow])
async def get_active_borrows(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    query = db.query(models.BookBorrow)
    if current_user.role == models.UserRole.STUDENT:
        query = query.filter(models.BookBorrow.user_id == current_user.id)
    return query.filter(models.BookBorrow.status != "Returned").all()
