import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

LOG_FILE = "logs/prediction_logs.csv"

st.title("ML Model Monitoring Dashboard")

if not os.path.exists(LOG_FILE):
    st.warning("No prediction logs found yet.")
else:

    df = pd.read_csv(LOG_FILE)

    st.subheader("Recent Predictions")
    st.dataframe(df.tail(20))

    st.subheader("Churn Prediction Distribution")

    fig, ax = plt.subplots()
    df["prediction"].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel("Prediction")
    ax.set_ylabel("Count")
    ax.set_title("Churn vs Non-Churn")

    st.pyplot(fig)

    st.subheader("Probability Distribution")

    fig2, ax2 = plt.subplots()
    df["probability"].hist(ax=ax2, bins=20)

    ax2.set_title("Churn Probability Distribution")

    st.pyplot(fig2)