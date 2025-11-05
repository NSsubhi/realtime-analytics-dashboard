#!/bin/bash
# Start script for FastAPI backend
uvicorn app.backend.main_simple:app --host 0.0.0.0 --port $PORT

