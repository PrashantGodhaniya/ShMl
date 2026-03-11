#!/bin/bash

echo "Starting SHML System..."

echo "Starting Customer Churn Prediction API..."
uvicorn api.app:app --host 0.0.0.0 --port 8010 --reload &

echo "Starting Real-time Monitoring Dashboard..."
streamlit run dashboard/realtime_dashboard.py --server.port 8501 --server.address 0.0.0.0 &

echo "--------------------------------------"
echo "SHML SYSTEM RUNNING"
echo "API Docs:"
echo "https://$(hostname)-8010.app.github.dev/docs"
echo ""
echo "Monitoring Dashboard:"
echo "https://$(hostname)-8501.app.github.dev"
echo "--------------------------------------"

wait