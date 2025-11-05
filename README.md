# Real-Time Analytics Dashboard with Kafka & Spark

## 🚀 Live Demo

**Live Dashboard**: [https://realtime-analytics-dashboard-production.up.railway.app/](https://realtime-analytics-dashboard-production.up.railway.app/)

## Overview
A real-time analytics dashboard that processes streaming data using Apache Kafka and Apache Spark. Includes simplified in-memory version for easy deployment.

## Features
- Real-time data streaming
- Event processing and aggregation
- Interactive analytics dashboard
- Multiple data sources (user events, transactions, logs)
- Real-time visualizations
- Simplified in-memory version (no Docker required)

## Tech Stack
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Data Processing**: Apache Spark (Structured Streaming)
- **Message Queue**: Apache Kafka (or in-memory for simplified version)
- **Database**: PostgreSQL (or in-memory for simplified version)
- **Visualization**: Plotly, Recharts

## Architecture
- **Full Version**: Kafka → Spark Streaming → PostgreSQL → FastAPI → Streamlit
- **Simplified Version**: In-memory data generator → FastAPI → Streamlit

## Local Development

### Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment:**
   - Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. **Start the backend (Terminal 1):**
   ```bash
   python app/backend/main_simple.py
   ```
   Backend will run on `http://localhost:8000` (or next available port)
   - API Docs: `http://localhost:8000/docs`

2. **Start the frontend (Terminal 2):**
   ```bash
   streamlit run app/frontend.py
   ```
   Frontend will run on `http://localhost:8501`

3. **Optional: Start data generator (Terminal 3):**
   ```bash
   python app/data_generator/generator_simple.py
   ```

## Deployment to Railway

### Quick Overview

Deploy all three services (Backend, Frontend, Data Generator) to Railway as separate services.

**📖 For detailed deployment instructions, see [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)**

### Prerequisites
- GitHub account
- Railway account (sign up at [railway.app](https://railway.app))

### Quick Steps

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy Backend Service (First Service):**
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project" → "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically use the `Procfile` for backend
   - **Copy the backend URL** (e.g., `https://your-backend.railway.app`)

3. **Deploy Frontend Service (Second Service):**
   - In the same Railway project, click "New Service"
   - Select same GitHub repo
   - **Start Command**: `streamlit run app/frontend.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`
   - **Environment Variable**: `API_URL` = your backend URL

4. **Deploy Data Generator Service (Third Service):**
   - In the same Railway project, click "New Service" again
   - Select same GitHub repo
   - **Start Command**: `python app/data_generator/generator_simple.py`
   - **Environment Variable**: `API_URL` = your backend URL

### Service URLs

**Live Demo**: [https://realtime-analytics-dashboard-production.up.railway.app/](https://realtime-analytics-dashboard-production.up.railway.app/)

After deployment:
- **Backend**: `https://your-backend.railway.app` (API Docs: `/docs`)
- **Frontend**: `https://your-frontend.railway.app` (Dashboard)
- **Data Generator**: Runs in background (no public URL)

### Notes
- All services use Railway's `PORT` environment variable automatically
- Frontend and Data Generator need `API_URL` environment variable pointing to backend
- The in-memory storage resets on each deployment restart
- For production, consider adding a database (PostgreSQL) service on Railway

**📖 See [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md) for detailed step-by-step instructions**

