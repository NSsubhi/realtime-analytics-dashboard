# Real-Time Analytics Dashboard with Kafka & Spark

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

### Prerequisites
- GitHub account
- Railway account (sign up at [railway.app](https://railway.app))

### Steps

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Railway:**
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect the Python project and use the `Procfile`
   - The backend API will be deployed and assigned a public URL

3. **Configure Environment Variables (if needed):**
   - In Railway project settings, add any required environment variables
   - For this simplified version, no additional environment variables are required

4. **Access Your API:**
   - Railway will provide a public URL (e.g., `https://your-app.railway.app`)
   - API Docs: `https://your-app.railway.app/docs`
   - Health Check: `https://your-app.railway.app/health`

### Notes
- The backend uses Railway's `PORT` environment variable automatically
- The in-memory storage resets on each deployment restart
- For production, consider adding a database (PostgreSQL) service on Railway

