import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="EcoPulse AI",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ EcoPulse AI")
st.subheader("AI-Powered Industrial Energy Optimization Platform")

API_URL = "http://127.0.0.1:8000/machines"

try:
    response = requests.get(API_URL)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Timestamp",
                "Machine ID",
                "Machine",
                "Voltage",
                "Current",
                "Power",
                "Temperature",
                "Efficiency",
                "Health",
                "Runtime"
            ]
        )

        st.success("Connected to FastAPI")

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.error("Could not fetch data from API")

except Exception:

    st.error("FastAPI server is not running.")