#!/bin/bash
# Start script for Streamlit frontend
streamlit run app/frontend.py --server.port $PORT --server.address 0.0.0.0 --server.headless true

