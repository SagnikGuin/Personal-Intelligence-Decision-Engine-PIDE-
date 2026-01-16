from utils import validators as vld
from utils import file_ops as flo
from utils import analytics as anal
from datetime import date
import os
import pandas as pd
import streamlit as st
flo.ensure_csv("data/activity_log.csv")
st.title("Personal Intelligence & Decision Engine")
name = st.text_input("What is your name?")
age = st.slider("What is your age?", 3, 100, 25)
activity_name = st.text_input("Enter the name of the activity")
hours = st.number_input("Enter number of hours", min_value=0.0, max_value=24.0)
energy = st.slider("Energy level", 1, 10, 4)
focus = st.slider("Focus Level", 1, 10, 4)
click_me = st.button('Confirm')
today = str(date.today())
if click_me:
    entry = {"name" : name, "age": age, "activity" : activity_name, "hours" : hours, "date": today, "focus": focus, "energy": energy}
    valid, msg = vld.validate_entry(entry)
    if not valid:
        st.error(msg)
    else:
        if not flo.append_csv("data/activity_log.csv", entry):
            st.error("Unable to save your entry. Please try again.")
        else:
            st.write("Your entered the following details")
            st.write(f"Name: {entry['name']}")
            st.write(f"Age: {entry['age']}")
            st.write(f"Activity Name: {entry['activity']}")
            st.write(f"Hours: {entry['hours']}")
            st.write(f"Date: {entry['date']}")
            st.write(f"Energy: {entry['energy']}")
            st.write(f"Focus: {entry['focus']}")
check_last_activities = st.button('Logged Activities')

if check_last_activities:
    df = flo.read_csv_safe("data/activity_log.csv")
    if df.empty:
        st.write("No data available")
    else:
        st.dataframe(df.tail(5))

df0 = flo.read_csv_safe("data/activity_log.csv")
st.subheader("📊 Your Activity Insights")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Hours", round(anal.get_total_hours(df0), 2))
with col2:
    st.metric("Avg Hours / Entry", round(anal.get_average_hours(df0), 2))

with col3:
    st.metric("Productivity Score", round(anal.get_productivity_score(df0), 2))

st.divider()
st.subheader("🗂 Activity Breakdown")
activity_map = anal.get_hours_by_activity(df0)
if activity_map:
    for activity, hours in activity_map.items():
        st.write(f"• {activity}: {round(hours, 2)} hours")
else:
    st.info("No activity data yet")