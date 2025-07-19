import streamlit as st
import joblib
from utils import preprocess_text_custom

# Load the model and vectorizer
model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit page config
st.set_page_config(page_title="Spam Detector", layout="centered")

# UI
st.title("📧 Email Spam Detector")
st.markdown("Paste any email content below to check if it's **SPAM** or **NOT SPAM**.")

# User input
email_input = st.text_area("✉️ Email content:", height=200)

# Prediction button
if st.button("🔍 Check"):
    if email_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Preprocess and predict
        clean_text = preprocess_text_custom(email_input)
        features = vectorizer.transform([clean_text])
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("🚨 This email is **SPAM**.")
        else:
            st.success("✅ This email is **NOT SPAM**.")
