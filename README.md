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

