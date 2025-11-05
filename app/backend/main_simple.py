"""
Simplified FastAPI Backend for Real-Time Analytics
In-memory version (no Kafka/PostgreSQL required)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Dict
from datetime import datetime, timedelta
import random
import logging
import socket

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Real-Time Analytics API",
    description="Simplified real-time analytics API (in-memory)",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
events_store: List[Dict] = []
metrics_store: Dict = {
    "total_events": 0,
    "events_per_minute": 0,
    "last_updated": datetime.now().isoformat()
}

def find_free_port(start_port=8000):
    """Find an available port"""
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return start_port

@app.get("/")
async def root():
    return {"message": "Real-Time Analytics API", "version": "simplified"}

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/events")
async def add_event(event: Dict):
    """Add event to store"""
    event["timestamp"] = datetime.now().isoformat()
    events_store.append(event)
    metrics_store["total_events"] += 1
    metrics_store["last_updated"] = datetime.now().isoformat()
    return {"status": "success", "event_id": len(events_store)}

@app.get("/api/events")
async def get_events(limit: int = 100):
    """Get recent events"""
    recent = events_store[-limit:] if len(events_store) > limit else events_store
    return {"events": recent, "count": len(recent)}

@app.get("/api/metrics")
async def get_metrics():
    """Get aggregated metrics"""
    now = datetime.now()
    one_minute_ago = now - timedelta(minutes=1)
    
    recent_events = [
        e for e in events_store 
        if datetime.fromisoformat(e.get("timestamp", now.isoformat())) > one_minute_ago
    ]
    
    metrics_store["events_per_minute"] = len(recent_events)
    
    return {
        "metrics": metrics_store,
        "recent_events_count": len(recent_events),
        "total_events": len(events_store)
    }

@app.get("/api/analytics")
async def get_analytics():
    """Get analytics data"""
    if not events_store:
        return {"analytics": {}}
    
    # Simple analytics
    event_types = {}
    for event in events_store[-1000:]:  # Last 1000 events
        event_type = event.get("type", "unknown")
        event_types[event_type] = event_types.get(event_type, 0) + 1
    
    return {
        "analytics": {
            "event_types": event_types,
            "total_events": len(events_store),
            "time_range": {
                "start": events_store[0]["timestamp"] if events_store else None,
                "end": events_store[-1]["timestamp"] if events_store else None
            }
        }
    }

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Use Railway PORT or find free port for local development
    port = int(os.getenv("PORT", find_free_port()))
    logger.info(f"Starting server on port {port}")
    logger.info(f"API docs: http://localhost:{port}/docs")
    uvicorn.run(app, host="0.0.0.0", port=port)

