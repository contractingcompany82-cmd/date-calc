import streamlit as st
from datetime import datetime, timedelta, date

st.set_page_config(page_title="Date & Age Calculator", page_icon="🗓️")

st.title("🗓️ Date & Age Calculator")

st.write("Select a date and number of days to calculate the future date.")
st.write("Or calculate your age by entering your date of birth.")

# ---------------- DATE CALCULATOR ----------------
st.subheader("📅 Future Date Calculator")

input_date = st.date_input("Select a date")
days = st.number_input("Enter number of days to add", min_value=0, step=1)

if st.button("Calculate Future Date"):
    result_date = input_date + timedelta(days=int(days))
    st.success(f"📅 **Result Date:** {result_date.strftime('%d-%m-%Y')}")

# ---------------- AGE CALCULATOR ----------------
st.subheader("👤 Age Calculator")

dob = st.date_input("Select your Date of Birth")

if st.button("Calculate Age"):
    today = date.today()

    if dob > today:
        st.error("Date of birth cannot be in the future.")
    else:
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            days += 30

        if months < 0:
            years -= 1
            months += 12

        st.success(
            f"🎉 **Your Age:** {years} years, {months} months, {days} days"
        )
