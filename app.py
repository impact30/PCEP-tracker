import streamlit as st
from datetime import date
from checklist import CHECKLIST_SECTIONS
from storage import load_data, save_data
from utils import render_progress_bar, calculate_timeline

DATA_PATH = "data/pcep_checklist.json"

st.set_page_config(page_title="PCEP Study Tracker", layout="wide")

st.title("📘 PCEP Study Progress Tracker")
st.write("Track your readiness for the PCEP certification exam.")

data = load_data(DATA_PATH)

# --- Date Setup ---
st.sidebar.header("⏳ Study Timeline")

col1, col2 = st.sidebar.columns(2)
start_date = col1.date_input("Start date", date.fromisoformat(data["start_date"]))
end_date = col2.date_input("Target date", date.fromisoformat(data["end_date"]))

data["start_date"] = start_date.isoformat()
data["end_date"] = end_date.isoformat()

timeline_info = calculate_timeline(start_date, end_date)
st.sidebar.info(timeline_info)

save_data(DATA_PATH, data)

# --- Progress Overview ---
st.subheader("📊 Overall Progress")
done_count = sum(item["done"] for s in data["sections"] for item in s["items"])
total_count = sum(len(s["items"]) for s in data["sections"])

st.write(render_progress_bar(done_count, total_count))

# --- Checklist Display ---
st.subheader("📋 Study Checklist")

for section_idx, section in enumerate(data["sections"]):
    with st.expander(section["name"], expanded=False):
        for item_idx, item in enumerate(section["items"]):
            checked = st.checkbox(
                item["text"],
                value=item["done"],
                key=f"{section_idx}-{item_idx}",
            )
            data["sections"][section_idx]["items"][item_idx]["done"] = checked

save_data(DATA_PATH, data)

st.success("Progress saved automatically.")
