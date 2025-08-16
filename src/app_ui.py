# app_ui.py
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analysis", page_icon="💡")

st.title("🔹 Sentiment Analysis Tool")
st.write("Enter some text below and find out whether it's Positive, Negative, or Neutral.")

# Input area
user_input = st.text_area("✍️ Enter your text here:")

if st.button("🔍 Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            st.success("✅ Sentiment: Positive 😀")
        elif polarity < 0:
            st.error("❌ Sentiment: Negative 😞")
        else:
            st.info("ℹ️ Sentiment: Neutral 😐")
