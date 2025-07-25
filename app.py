import streamlit as st
import pandas as pd
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Hello Neighbor", page_icon="🫂", layout="centered")

# --- LOGO & TITLE ---
st.image("maybelogo.png", width=200)  # replace with your logo file name
st.title("Hello Neighbor 👋")
st.write("A Community Skill‑Share Circle — Learn • Share • Connect")

st.markdown("---")

# --- EVENT LIST ---
st.header("Upcoming Skill Share Sessions 📅")

# Load events from a CSV or create a starter DataFrame
try:
    events = pd.read_csv("events.csv")
except FileNotFoundError:
    events = pd.DataFrame([
        {"Date": "2025-08-10", "Topic": "Intro to Python", "Location": "Local Library"},
        {"Date": "2025-08-17", "Topic": "Budgeting Basics", "Location": "Community Center"},
    ])

# Display events
for _, row in events.iterrows():
    date_str = datetime.strptime(row["Date"], "%Y-%m-%d").strftime("%b %d, %Y")
    st.markdown(f"**{date_str}** — *{row['Topic']}* at {row['Location']}")

st.markdown("---")

# --- SIGN UP TO TEACH ---
st.header("Want to teach a skill?")
with st.form("teach_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    skill = st.text_input("What skill could you teach?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Save to a CSV (append mode)
        with open("teach_signups.csv", "a") as f:
            f.write(f"{name},{email},{skill}\n")
        st.success("Thank you! We'll reach out soon.")

st.markdown("---")

# --- SUGGEST A TOPIC ---
st.header("Suggest a skill to learn!")
with st.form("suggest_form"):
    sugg_name = st.text_input("Your Name (optional)")
    suggestion = st.text_area("What skill would you like to learn?")
    sugg_submit = st.form_submit_button("Submit Suggestion")
    if sugg_submit:
        with open("skill_suggestions.csv", "a") as f:
            f.write(f"{sugg_name},{suggestion}\n")
        st.success("Suggestion received! Thank you.")
