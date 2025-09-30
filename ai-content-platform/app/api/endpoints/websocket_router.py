from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Query
from typing import Dict, Set
import json

from app.websockets.manager import ConnectionManager
from app.core.security import decode_token

router = APIRouter()

# Global connection manager
manager = ConnectionManager()


@router.websocket("/stream/{session_id}")
async def websocket_stream_endpoint(
    websocket: WebSocket,
    session_id: str,
    token: str = Query(...)
):
    """WebSocket endpoint for real-time AI streaming."""
    # Validate token
    payload = decode_token(token)
    if not payload:
        await websocket.close(code=1008, reason="Invalid token")
        return
    
    user_id = int(payload.get("sub"))
    
    # Accept connection
    await manager.connect(websocket, session_id, user_id)
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Echo back for now (implement actual AI streaming logic)
            await manager.send_personal_message(
                {"type": "ack", "message": "Received"},
                session_id
            )
            
            # Example: broadcast to all connections for collaboration
            if message.get("broadcast"):
                await manager.broadcast(
                    {"type": "update", "data": message.get("content")},
                    session_id
                )
    
    except WebSocketDisconnect:
        manager.disconnect(session_id)
        await manager.broadcast(
            {"type": "user_left", "session": session_id},
            session_id
        )
    except Exception as e:
        await manager.send_personal_message(
            {"type": "error", "message": str(e)},
            session_id
        )
        manager.disconnect(session_id)


@router.websocket("/collaborate/{room_id}")
async def websocket_collaboration_endpoint(
    websocket: WebSocket,
    room_id: str,
    token: str = Query(...)
):
    """WebSocket endpoint for real-time collaboration."""
    # Validate token
    payload = decode_token(token)
    if not payload:
        await websocket.close(code=1008, reason="Invalid token")
        return
    
    user_id = int(payload.get("sub"))
    
    # Accept connection
    await manager.connect(websocket, room_id, user_id)
    
    try:
        # Notify others of new user
        await manager.broadcast(
            {"type": "user_joined", "user_id": user_id},
            room_id
        )
        
        while True:
            # Receive collaborative edits
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Broadcast changes to all users in room
            await manager.broadcast(
                {
                    "type": "edit",
                    "user_id": user_id,
                    "changes": message.get("changes")
                },
                room_id
            )
    
    except WebSocketDisconnect:
        manager.disconnect(room_id)
        await manager.broadcast(
            {"type": "user_left", "user_id": user_id},
            room_id
        )
