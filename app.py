import streamlit as st
import joblib
import numpy as np
import os

# ------------------ Credentials with Roles ------------------
USER_CREDENTIALS = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user456", "role": "user"},
    "user2": {"password": "user789", "role": "user"}
}

# ------------------ Session State Setup ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None

# ------------------ Login UI ------------------
def login():
    st.title("🔐 Login to Churn Predictor")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username]["password"] == password:
            st.success("Login successful!")
            st.session_state.logged_in = True
            st.session_state.role = USER_CREDENTIALS[username]["role"]
            st.rerun()
        else:
            st.error("Invalid username or password")

# ------------------ Main App with Admin Controls ------------------
def main_app():
    st.title("Smart Churn Predictor: Retain Customers Before They Leave")
    st.sidebar.markdown(f"👋 Logged in as: **{st.session_state.role.upper()}**")

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.success("You have been logged out.")
        st.rerun()

    st.divider()

    # Admin features
    if st.session_state.role == "admin":
        st.sidebar.subheader("👑 Admin Controls")
        with st.sidebar.expander("📤 Upload New Model or Scaler"):
            uploaded_model = st.file_uploader("Upload new model.pkl", type="pkl")
            uploaded_scaler = st.file_uploader("Upload new scaler.pkl", type="pkl")
            if uploaded_model and uploaded_scaler:
                with open("model.pkl", "wb") as f:
                    f.write(uploaded_model.read())
                with open("scaler.pkl", "wb") as f:
                    f.write(uploaded_scaler.read())
                st.sidebar.success("✅ Model and Scaler updated!")
                st.rerun()
    else:
        st.sidebar.info("Logged in as regular user. Admin privileges not available.")

    # Load model and scaler
    if os.path.exists("scaler.pkl") and os.path.exists("model.pkl"):
        scaler = joblib.load("scaler.pkl")
        model = joblib.load("model.pkl")
    else:
        st.error("Model or scaler files are missing!")
        return

    st.write("Please enter the values and hit the predict button for getting a prediction.")
    st.divider()

    # User Inputs
    age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)
    tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)
    monthlycharge = st.number_input("Enter Monthly Charge", min_value=30, max_value=150)
    gender = st.selectbox("Enter the Gender", ["Male", "Female"])

    st.divider()

    # Prediction
    if st.button("Predict!"):
        gender_selected = 1 if gender == "Female" else 0
        X = [age, gender_selected, tenure, monthlycharge]
        X_array = scaler.transform([np.array(X)])

        prediction = model.predict(X_array)[0]
        predicted = "Yes" if prediction == 1 else "No"

        st.subheader(f"Predicted Churn: {predicted}")

        if predicted == "Yes":
            st.warning("⚠️ High risk of churn detected!")
            st.subheader("💡 Suggested Retention Strategies")

            # 📌 Billing & Plan Adjustments
            st.markdown("### 💸 Billing & Plan Adjustments")
            if monthlycharge > 100:
                st.markdown("- Offer a **flexible billing plan** or introduce a **loyalty discount**.")
            if tenure < 12:
                st.markdown("- Provide **limited-time onboarding rewards** to encourage early loyalty.")

            # 📌 Personalized Offers
            st.markdown("### 🎯 Personalized Offers")
            if age < 25:
                st.markdown("- Promote **youth-centric bundles** with OTT platforms, high-speed data, and gaming perks.")
            if gender_selected == 1:
                st.markdown("- Send **emotionally intelligent campaigns** — female users tend to value empathy-driven messaging.")

            # 📌 Retention Tactics
            st.markdown("### 🤝 Engagement & Support")
            st.markdown("- Implement **24/7 proactive customer support**.")
            st.markdown("- Launch a **feedback campaign** to collect pain points and act on them.")
            st.markdown("- Introduce **contract benefits or upgrades** that enhance perceived value.")

            st.markdown("> 💬 _Don’t let valuable customers slip away. Act before they churn._")
            st.balloons()
        else:
            st.success("✅ The customer is likely to stay. Keep them engaged!")

# ------------------ Show Login or App ------------------
if not st.session_state.logged_in:
    login()
else:
    main_app()
