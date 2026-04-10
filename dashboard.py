import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI Usage Dashboard", layout="wide")

st.title("AI Usage Tracker Dashboard")

API_URL = "http://127.0.0.1:8000/dashboard"

# Refresh Button
if st.button("Refresh Data"):
    st.rerun()

try:
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        col1, col2, col3 = st.columns(3)

        # 🔹 OpenAI Section
        with col1:
            st.subheader("OpenAI")

            openai_data = data.get("openai", {})

            if openai_data.get("status") == "error":
                st.error("Quota exceeded / API issue")
            else:
                st.success("API Working")
                st.write(openai_data)

        # 🔹 TTS Section
        with col2:
            st.subheader("Text-to-Speech")

            tts = data.get("tts", {})
            usage = tts.get("usage", {})

            st.metric("Characters Used", usage.get("characters_used", 0))
            st.metric("Cost ($)", usage.get("cost", 0))
            st.metric("Remaining Credits", usage.get("remaining_credits", 0))

        # 🔹 STT Section
        with col3:
            st.subheader("Speech-to-Text")

            stt = data.get("stt", {})
            usage = stt.get("usage", {})

            st.metric("Minutes Processed", usage.get("minutes_processed", 0))
            st.metric("Cost ($)", usage.get("cost", 0))
            st.metric("Remaining Credits", usage.get("remaining_credits", 0))

        #  Chart Section
        st.subheader("Usage Overview")

        chart_data = pd.DataFrame({
            "Service": ["OpenAI", "TTS", "STT"],
            "Usage": [
                0 if data["openai"]["status"] == "error" else 10,
                data["tts"]["usage"]["characters_used"],
                data["stt"]["usage"]["minutes_processed"]
            ]
        })

        st.bar_chart(chart_data.set_index("Service"))

    else:
        st.error(f"API Error: {response.status_code}")

except Exception as e:
    st.error(f"Connection Error: {e}")