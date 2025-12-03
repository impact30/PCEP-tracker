import streamlit as st
from datetime import date
from checklist import CHECKLIST_SECTIONS
from storage import load_data, save_data
from utils import (
    render_progress_bar,
    render_expander_header_style,
    calculate_timeline
)

DATA_PATH = "data/pcep_checklist.json"

# Page config
st.set_page_config(page_title="PCEP Tracker", layout="wide")

st.title("📘 PCEP Study Progress Tracker")
st.write("Each section header fills with color according to your progress.")

# Load data
data = load_data(DATA_PATH)

# ======================================================
# Sidebar: Study Timeline
# ======================================================
st.sidebar.header("⏳ Study Timeline")

default_start = data.get("start_date", date.today().isoformat())
default_end = data.get("end_date", date.today().isoformat())

col1, col2 = st.sidebar.columns(2)
start_date = col1.date_input("Start", date.fromisoformat(default_start))
end_date = col2.date_input("Target", date.fromisoformat(default_end))

data["start_date"] = start_date.isoformat()
data["end_date"] = end_date.isoformat()

st.sidebar.info(calculate_timeline(start_date, end_date))

save_data(DATA_PATH, data)

# ======================================================
# Global Progress
# ======================================================
st.subheader("📊 Overall Progress")

done_count = sum(item["done"] for s in data["sections"] for item in s["items"])
total_count = sum(len(s["items"]) for s in data["sections"])

st.write(render_progress_bar(done_count, total_count))

# ======================================================
# Checklist Sections
# ======================================================
st.subheader("📋 Study Checklist")

for section_idx, section in enumerate(data["sections"]):
    items = section["items"]
    done = sum(1 for i in items if i["done"])
    total = len(items)
    percent = int((done / total) * 100) if total else 0

    # Inject correct CSS styling for the header
    st.markdown(
        render_expander_header_style(section_idx, percent),
        unsafe_allow_html=True
    )

    with st.expander(section["name"], expanded=False):

        # Marker so CSS can identify which header to color
        st.markdown(
            f'<div section-marker="{section_idx}"></div>',
            unsafe_allow_html=True
        )

        # Checkboxes with instant update
        for item_idx, item in enumerate(items):
            checked = st.checkbox(
                item["text"],
                value=item["done"],
                key=f"{section_idx}-{item_idx}"
            )

            # Only react if the value changed
            if checked != item["done"]:
                item["done"] = checked
                save_data(DATA_PATH, data)
                st.rerun()  # 👈 instant refresh for animation

# Save progress
save_data(DATA_PATH, data)

st.success("Progress saved.")
