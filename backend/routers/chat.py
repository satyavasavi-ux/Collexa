from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from typing import List, Optional
import datetime
import models, schemas, database, dependencies
from websocket_manager import manager

router = APIRouter()

@router.get("/channels", response_model=List[schemas.ChatChannel])
async def list_channels(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    return db.query(models.ChatChannel).all()

@router.post("/channels", response_model=schemas.ChatChannel)
async def create_channel(
    channel_in: schemas.ChatChannelCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    existing = db.query(models.ChatChannel).filter(models.ChatChannel.name == channel_in.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Channel with this name already exists")
    ch = models.ChatChannel(
        name=channel_in.name,
        description=channel_in.description,
        is_private=channel_in.is_private,
        created_by=current_user.id
    )
    db.add(ch)
    db.commit()
    db.refresh(ch)
    return ch

@router.get("/channels/{channel_id}/messages", response_model=List[schemas.ChatMessage])
async def get_channel_messages(
    channel_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    return db.query(models.ChatMessage).filter(models.ChatMessage.channel_id == channel_id).order_by(models.ChatMessage.sent_at.asc()).limit(100).all()

@router.post("/channels/{channel_id}/messages", response_model=schemas.ChatMessage)
async def send_message(
    channel_id: int,
    msg_in: schemas.ChatMessageCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    msg = models.ChatMessage(
        channel_id=channel_id,
        sender_id=current_user.id,
        content=msg_in.content,
        attachment_url=msg_in.attachment_url,
        sent_at=datetime.datetime.utcnow()
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)

    await manager.broadcast_to_channel(channel_id, {
        "type": "NEW_CHAT_MESSAGE",
        "channel_id": channel_id,
        "sender": current_user.name,
        "sender_id": current_user.id,
        "content": msg.content,
        "sent_at": str(msg.sent_at)
    })

    return msg
