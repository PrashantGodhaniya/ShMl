import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="SHML Monitoring Dashboard",
    layout="wide"
)

st.title("SHML - ML Model Monitoring Dashboard")

log_file = "logs/prediction_logs.csv"

if not os.path.exists(log_file):

    st.warning("No prediction logs found yet. Run the API prediction first.")

else:

    df = pd.read_csv(log_file)

    st.subheader("Recent Predictions")

    st.dataframe(df.tail(20), use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Churn Prediction Distribution")

        churn_counts = df["prediction"].value_counts()

        st.bar_chart(churn_counts)

    with col2:

        st.subheader("Prediction Probability Trend")

        st.line_chart(df["probability"])

    st.subheader("Prediction Probability Over Time")

    if "timestamp" in df.columns:

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        df = df.sort_values("timestamp")

        st.line_chart(df.set_index("timestamp")["probability"])

    st.subheader("Dataset Summary")

    st.write("Total Predictions:", len(df))

    churn_rate = df["prediction"].mean()

    st.write("Churn Rate:", round(churn_rate, 3))