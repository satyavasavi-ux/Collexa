from fastapi import WebSocket
from typing import List, Dict, Set, Optional, Any
import json
import asyncio

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.user_connections: Dict[int, List[WebSocket]] = {}
        self.channel_subscriptions: Dict[int, Set[WebSocket]] = {}
        self.active_sessions: Dict[int, dict] = {}

    async def connect(self, websocket: WebSocket, user_id: Optional[int] = None):
        await websocket.accept()
        self.active_connections.append(websocket)
        if user_id:
            if user_id not in self.user_connections:
                self.user_connections[user_id] = []
            self.user_connections[user_id].append(websocket)

    def disconnect(self, websocket: WebSocket, user_id: Optional[int] = None):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        if user_id and user_id in self.user_connections:
            if websocket in self.user_connections[user_id]:
                self.user_connections[user_id].remove(websocket)
            if not self.user_connections[user_id]:
                del self.user_connections[user_id]
        
        # Remove from channel subscriptions
        for ch_id in list(self.channel_subscriptions.keys()):
            if websocket in self.channel_subscriptions[ch_id]:
                self.channel_subscriptions[ch_id].discard(websocket)

    def start_session(self, teacher_id: int, session_data: dict):
        self.active_sessions[teacher_id] = session_data

    def get_session(self, teacher_id: int) -> Optional[dict]:
        return self.active_sessions.get(teacher_id)

    def end_session(self, teacher_id: int):
        if teacher_id in self.active_sessions:
            del self.active_sessions[teacher_id]

    async def broadcast(self, message: Any):
        msg_str = json.dumps(message) if not isinstance(message, str) else message
        dead_connections = []
        for connection in self.active_connections:
            try:
                await connection.send_text(msg_str)
            except Exception:
                dead_connections.append(connection)
        for dead in dead_connections:
            if dead in self.active_connections:
                self.active_connections.remove(dead)

    async def notify_user(self, user_id: int, message: Any):
        await self.send_personal_message(message, user_id)

    async def send_personal_message(self, message: Any, user_id: int):
        if user_id not in self.user_connections:
            return
        msg_str = json.dumps(message) if not isinstance(message, str) else message
        dead_connections = []
        for connection in self.user_connections[user_id]:
            try:
                await connection.send_text(msg_str)
            except Exception:
                dead_connections.append(connection)
        for dead in dead_connections:
            if dead in self.user_connections[user_id]:
                self.user_connections[user_id].remove(dead)

    def subscribe_channel(self, channel_id: int, websocket: WebSocket):
        if channel_id not in self.channel_subscriptions:
            self.channel_subscriptions[channel_id] = set()
        self.channel_subscriptions[channel_id].add(websocket)

    async def broadcast_to_channel(self, channel_id: int, message: Any):
        if channel_id not in self.channel_subscriptions:
            return
        msg_str = json.dumps(message) if not isinstance(message, str) else message
        dead = []
        for ws in self.channel_subscriptions[channel_id]:
            try:
                await ws.send_text(msg_str)
            except Exception:
                dead.append(ws)
        for d in dead:
            self.channel_subscriptions[channel_id].discard(d)

manager = ConnectionManager()
