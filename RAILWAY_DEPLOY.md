# Railway Deployment Guide - All Services

This guide explains how to deploy all three services (Backend, Frontend, Data Generator) to Railway.

## 🚀 Deployment Strategy

Railway supports multiple services from the same repository. You'll create three separate services:

1. **Backend Service** - FastAPI API
2. **Frontend Service** - Streamlit Dashboard
3. **Data Generator Service** - Background worker that generates events

## 📋 Step-by-Step Deployment

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Real-time analytics dashboard"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Deploy Backend Service (First Service)

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository
5. Railway will automatically detect Python and use the `Procfile`
6. The backend will be deployed and assigned a URL like `https://your-backend.railway.app`
7. **Copy this URL** - you'll need it for the other services

### 3. Deploy Frontend Service (Second Service)

1. In the same Railway project, click **"New Service"**
2. Select **"GitHub Repo"** and choose the same repository
3. In the service settings:
   - **Name**: `frontend` (or any name you prefer)
   - **Start Command**: 
     ```
     streamlit run app/frontend.py --server.port $PORT --server.address 0.0.0.0 --server.headless true
     ```
   - **Environment Variables**:
     - `API_URL`: Set this to your backend service URL (e.g., `https://your-backend.railway.app`)
4. Railway will deploy the frontend and assign a URL like `https://your-frontend.railway.app`

### 4. Deploy Data Generator Service (Third Service)

1. In the same Railway project, click **"New Service"** again
2. Select **"GitHub Repo"** and choose the same repository
3. In the service settings:
   - **Name**: `data-generator` (or any name you prefer)
   - **Start Command**: 
     ```
     python app/data_generator/generator_simple.py
     ```
   - **Environment Variables**:
     - `API_URL`: Set this to your backend service URL (e.g., `https://your-backend.railway.app`)
4. Railway will deploy the data generator as a background worker

## 🔗 Service URLs

After deployment, you'll have three URLs:

- **Backend**: `https://your-backend.railway.app`
  - API Docs: `https://your-backend.railway.app/docs`
  - Health Check: `https://your-backend.railway.app/health`

- **Frontend**: `https://your-frontend.railway.app`
  - Dashboard: `https://your-frontend.railway.app`

- **Data Generator**: Runs in background (no public URL)

## 🔧 Environment Variables

### Backend Service
- No environment variables required (uses Railway's `PORT` automatically)

### Frontend Service
- `API_URL`: Backend service URL (e.g., `https://your-backend.railway.app`)

### Data Generator Service
- `API_URL`: Backend service URL (e.g., `https://your-backend.railway.app`)

## 🎯 Quick Setup Checklist

- [ ] Push code to GitHub
- [ ] Create Railway project
- [ ] Deploy backend service (first service)
- [ ] Copy backend URL
- [ ] Deploy frontend service with `API_URL` environment variable
- [ ] Deploy data generator service with `API_URL` environment variable
- [ ] Access frontend dashboard
- [ ] Verify data generator is sending events

## 💡 Tips

1. **Service Discovery**: Railway services in the same project can reference each other using the service name. However, for simplicity, using the public URL is recommended.

2. **Environment Variables**: You can set environment variables in Railway dashboard:
   - Go to each service
   - Click on "Variables" tab
   - Add `API_URL` with your backend URL

3. **Port Binding**: All services automatically use Railway's `PORT` environment variable.

4. **Monitoring**: Check Railway logs for each service to see if they're running correctly.

5. **Data Generator**: The data generator will continuously send events to your backend. You can check the logs to see event generation activity.

## 🔄 Updating Services

When you push changes to GitHub:
- Railway will automatically redeploy all services
- Each service will restart with the latest code
- Environment variables are preserved

## 📊 Accessing Your Dashboard

1. Open your frontend URL in a browser
2. The dashboard will automatically connect to the backend
3. The data generator will start sending events
4. You should see real-time metrics and analytics

## 🐛 Troubleshooting

- **Frontend can't connect to backend**: Check that `API_URL` is set correctly
- **Data generator not sending events**: Check that `API_URL` is set correctly and backend is running
- **Services not starting**: Check Railway logs for error messages
- **Port issues**: Railway handles ports automatically via `$PORT` variable

