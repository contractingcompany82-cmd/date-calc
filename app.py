import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Date Calculator", page_icon="🗓️")

st.title("🗓️ Date Calculator")

st.write("Enter a date and number of days to calculate the future date.")

# Input date
input_date = st.date_input("Select a date")

# Input number of days
days = st.number_input("Enter number of days to add", min_value=0, step=1)

# Calculate
if st.button("Calculate"):
    result_date = input_date + timedelta(days=int(days))
    st.success(f"📅 **Result Date:** {result_date.strftime('%d-%m-%Y')}")
