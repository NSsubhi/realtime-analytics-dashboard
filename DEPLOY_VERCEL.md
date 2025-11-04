# Deploy to Vercel - Real-Time Analytics Dashboard

## 🚀 Deployment Strategy

### What Can Be Deployed to Vercel

✅ **Frontend (Streamlit)** → Convert to React/Next.js for Vercel  
✅ **FastAPI Backend** → Deploy as Vercel Serverless Functions  
❌ **Kafka/Spark** → Need external cloud services  

### Architecture for Vercel Deployment

```
Frontend (Next.js/React) → Vercel
     ↓
API (FastAPI Serverless) → Vercel
     ↓
External Services:
- Kafka: Confluent Cloud / AWS MSK
- Database: PostgreSQL (Railway/Neon/Supabase)
- Redis: Upstash Redis
```

## 📋 Step-by-Step Deployment

### Option 1: Full Stack on Vercel (Recommended)

#### 1. Convert Frontend to Next.js

Create a Next.js app instead of Streamlit:
- Better Vercel support
- Faster page loads
- Better SEO

#### 2. Deploy FastAPI as Serverless Functions

Vercel supports Python serverless functions:
- Create `api/` directory
- Each endpoint becomes a serverless function
- Auto-scales with traffic

#### 3. Use External Services

**Kafka:**
- Confluent Cloud (free tier available)
- AWS MSK (managed Kafka)
- Upstash Kafka (serverless)

**Database:**
- Railway PostgreSQL (free tier)
- Neon PostgreSQL (serverless)
- Supabase (free tier)

**Redis:**
- Upstash Redis (serverless, free tier)
- Redis Cloud (free tier)

### Option 2: Hybrid (Simpler)

**Frontend + API → Vercel**  
**Kafka/Spark → Keep local or use cloud**

## 🛠️ Setup for Vercel

### 1. Create `vercel.json`

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/**/*.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "api/$1.py"
    }
  ]
}
```

### 2. Create API Directory Structure

```
api/
├── index.py          # FastAPI app
├── metrics.py        # /api/metrics endpoint
├── realtime.py       # /api/realtime endpoint
└── stats.py          # /api/stats endpoint
```

### 3. Environment Variables on Vercel

Set these in Vercel dashboard:
- `KAFKA_BOOTSTRAP_SERVERS` (Confluent Cloud)
- `POSTGRES_HOST` (Railway/Neon)
- `REDIS_HOST` (Upstash)

### 4. Deploy Frontend

**Next.js Example:**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

**Or connect GitHub repo:**
- Push to GitHub
- Connect repo in Vercel dashboard
- Auto-deploy on push

## 📊 Recommended Services

### Free Tier Options:

1. **Kafka**: Confluent Cloud (free tier: 5GB/month)
2. **PostgreSQL**: Railway (free tier: $5/month credit)
3. **Redis**: Upstash (free tier: 10K commands/day)
4. **Frontend + API**: Vercel (free tier: generous)

## 🎯 Quick Deploy Checklist

- [ ] Convert Streamlit to Next.js/React
- [ ] Split FastAPI into serverless functions
- [ ] Set up Confluent Cloud Kafka
- [ ] Set up PostgreSQL (Railway/Neon)
- [ ] Set up Redis (Upstash)
- [ ] Create `vercel.json`
- [ ] Set environment variables
- [ ] Deploy to Vercel

## 💡 Alternative: Railway Deployment

Railway supports:
- ✅ Docker containers (full stack)
- ✅ PostgreSQL
- ✅ Redis
- ✅ Kafka (via Docker)

**Better for:** Full stack with Kafka/Spark  
**Vercel is better for:** Frontend + API only

## 🚀 Next Steps

1. **Test locally** with simplified version
2. **Choose deployment strategy** (Vercel or Railway)
3. **Set up cloud services** (Kafka, Database, Redis)
4. **Deploy frontend + API** to Vercel
5. **Connect to cloud services**

Would you like me to:
- Create Next.js frontend?
- Convert FastAPI to Vercel serverless functions?
- Set up configuration for cloud services?

