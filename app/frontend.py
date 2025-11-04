"""
Streamlit Frontend for Real-Time Analytics Dashboard
"""

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import os

# Page config
st.set_page_config(
    page_title="Real-Time Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# API URL
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'auto_refresh' not in st.session_state:
    st.session_state.auto_refresh = False

# Sidebar
with st.sidebar:
    st.title("📊 Real-Time Analytics")
    
    # API URL input
    api_url_input = st.text_input("🌐 API URL", value=API_URL)
    if api_url_input != API_URL:
        API_URL = api_url_input
    
    # Auto-refresh
    st.session_state.auto_refresh = st.checkbox("🔄 Auto-refresh (5s)", value=False)
    
    # Manual refresh
    if st.button("🔄 Refresh Now"):
        st.rerun()

# Main dashboard
st.title("📊 Real-Time Analytics Dashboard")

# Check API connection
try:
    health = requests.get(f"{API_URL}/health", timeout=2)
    if health.status_code == 200:
        st.success("✅ Connected to API")
    else:
        st.error("❌ API not responding")
        st.stop()
except:
    st.error(f"❌ Cannot connect to API at {API_URL}")
    st.info("💡 Make sure the backend is running: `python app/backend/main_simple.py`")
    st.stop()

# Metrics
col1, col2, col3, col4 = st.columns(4)

try:
    metrics = requests.get(f"{API_URL}/api/metrics", timeout=5).json()
    metrics_data = metrics.get("metrics", {})
    
    with col1:
        st.metric("Total Events", metrics_data.get("total_events", 0))
    
    with col2:
        st.metric("Events/min", metrics_data.get("events_per_minute", 0))
    
    with col3:
        st.metric("Recent Events", metrics.get("recent_events_count", 0))
    
    with col4:
        last_updated = metrics_data.get("last_updated", "N/A")
        st.metric("Last Updated", last_updated.split("T")[1][:8] if "T" in last_updated else "N/A")
except Exception as e:
    st.error(f"Error fetching metrics: {e}")

st.markdown("---")

# Analytics
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Event Types Distribution")
    try:
        analytics = requests.get(f"{API_URL}/api/analytics", timeout=5).json()
        event_types = analytics.get("analytics", {}).get("event_types", {})
        
        if event_types:
            df = pd.DataFrame(list(event_types.items()), columns=["Event Type", "Count"])
            fig = px.pie(df, values="Count", names="Event Type", title="Event Distribution")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No events yet. Start the data generator!")
    except Exception as e:
        st.error(f"Error: {e}")

with col2:
    st.subheader("📊 Recent Events")
    try:
        events = requests.get(f"{API_URL}/api/events", params={"limit": 10}, timeout=5).json()
        events_list = events.get("events", [])
        
        if events_list:
            df = pd.DataFrame(events_list)
            st.dataframe(df[["type", "user_id", "timestamp"]].head(10), use_container_width=True)
        else:
            st.info("No events yet.")
    except Exception as e:
        st.error(f"Error: {e}")

# Auto-refresh
if st.session_state.auto_refresh:
    time.sleep(5)
    st.rerun()

# Instructions
with st.expander("ℹ️ How to Use"):
    st.markdown("""
    1. **Start Backend**: `python app/backend/main_simple.py`
    2. **Start Data Generator** (optional): `python app/data_generator/generator_simple.py`
    3. **View Dashboard**: This page will auto-refresh if enabled
    """)

