from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal
import datetime
import models, schemas, database, dependencies

router = APIRouter()

@router.get("/hostels", response_model=List[schemas.Hostel])
async def list_hostels(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    return db.query(models.Hostel).all()

@router.post("/hostels", response_model=schemas.Hostel)
async def create_hostel(
    hostel_in: schemas.HostelCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["HOSTEL", "ADMIN"]))
):
    hostel = models.Hostel(**hostel_in.dict())
    db.add(hostel)
    db.commit()
    db.refresh(hostel)
    return hostel

@router.post("/rooms", response_model=schemas.HostelRoom)
async def add_room(
    room_in: schemas.HostelRoomCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["HOSTEL", "ADMIN"]))
):
    room = models.HostelRoom(**room_in.dict())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

@router.post("/rooms/{room_id}/allot")
async def allot_room(
    room_id: int,
    student_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["HOSTEL", "ADMIN"]))
):
    room = db.query(models.HostelRoom).filter(models.HostelRoom.id == room_id).first()
    if not room or room.occupied_count >= room.capacity:
        raise HTTPException(status_code=400, detail="Room is not available or at full capacity")
    
    student = db.query(models.Student).filter(models.Student.user_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student record not found")

    student.hostel_room_id = room.id
    room.occupied_count += 1
    db.commit()
    return {"message": f"Room {room.room_number} allotted to student successfully."}

@router.get("/bus-routes", response_model=List[schemas.BusRoute])
async def list_bus_routes(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    return db.query(models.BusRoute).all()

@router.post("/bus-routes", response_model=schemas.BusRoute)
async def create_bus_route(
    route_in: schemas.BusRouteCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["TRANSPORT", "ADMIN"]))
):
    route = models.BusRoute(**route_in.dict())
    db.add(route)
    db.commit()
    db.refresh(route)
    return route

@router.post("/passes/issue", response_model=schemas.TransportPass)
async def issue_transport_pass(
    pass_in: schemas.TransportPassCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.RoleChecker(["TRANSPORT", "ADMIN"]))
):
    tpass = models.TransportPass(
        student_id=pass_in.student_id,
        route_id=pass_in.route_id,
        pass_number=pass_in.pass_number,
        valid_from=pass_in.valid_from,
        valid_until=pass_in.valid_until or (datetime.date.today() + datetime.timedelta(days=180)),
        amount_paid=pass_in.amount_paid,
        status="Active"
    )
    db.add(tpass)
    db.commit()
    db.refresh(tpass)
    return tpass
