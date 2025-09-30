from typing import Dict, List
from fastapi import WebSocket
import json


class ConnectionManager:
    """Manager for WebSocket connections."""
    
    def __init__(self):
        # session_id -> list of connections
        self.active_connections: Dict[str, List[tuple[WebSocket, int]]] = {}
    
    async def connect(self, websocket: WebSocket, session_id: str, user_id: int):
        """Accept and store a new WebSocket connection."""
        await websocket.accept()
        if session_id not in self.active_connections:
            self.active_connections[session_id] = []
        self.active_connections[session_id].append((websocket, user_id))
    
    def disconnect(self, session_id: str):
        """Remove a connection."""
        if session_id in self.active_connections:
            del self.active_connections[session_id]
    
    async def send_personal_message(self, message: dict, session_id: str):
        """Send message to a specific session."""
        if session_id in self.active_connections:
            for websocket, _ in self.active_connections[session_id]:
                await websocket.send_text(json.dumps(message))
    
    async def broadcast(self, message: dict, session_id: str):
        """Broadcast message to all connections in a session."""
        if session_id in self.active_connections:
            for websocket, _ in self.active_connections[session_id]:
                await websocket.send_text(json.dumps(message))
    
    async def broadcast_all(self, message: dict):
        """Broadcast message to all active connections."""
        for connections in self.active_connections.values():
            for websocket, _ in connections:
                await websocket.send_text(json.dumps(message))
