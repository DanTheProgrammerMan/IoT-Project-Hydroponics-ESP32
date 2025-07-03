# utils.py

import streamlit as st
import os
import datetime
from zoneinfo import ZoneInfo

# Apply CSS Styles to all Pages
def apply_css(file_name: str):
    css_path = os.path.join("styles", file_name)
    try:
        with open(css_path, encoding="utf-8") as f:
            css = f.read()
    except UnicodeDecodeError:
        with open(css_path, encoding="latin-1") as f:
            css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# # Gets time and runs st.rerun() every 10 minutes on some pages
# def get_time_and_rerun_every_10(timezone: str = "Australia/Perth") -> str:
#     """
#     Returns current time "HH:MM:SS" in 24-hour format for the given timezone.
#     Triggers st.rerun() once each time the clock hits a
#     multiple of 10 minutes (00,10,20,30,40,50).
#     """
#     # 1) Fetch Zone/Time now
#     tz = ZoneInfo(timezone)
#     now = datetime.datetime.now(tz)
#     formatted = now.strftime("%H:%M:%S")

#     # 2) Initialize our “last rerun” marker
#     if "last_rerun_minute" not in st.session_state:
#         st.session_state.last_rerun_minute = now.minute

#     # 3) Check for a new 10-minute mark
#     if now.minute % 10 == 0 and now.minute != st.session_state.last_rerun_minute:
#         st.session_state.last_rerun_minute = now.minute
#         st.rerun()

#     return formatted