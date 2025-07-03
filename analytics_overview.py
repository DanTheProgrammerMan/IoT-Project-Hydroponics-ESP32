# analytics_overview.py

import streamlit as st
from datetime import datetime, timedelta, timezone
import os
import pandas as pd

DATA_FILE = 'sensor_data.csv'

st.title("Analytics Overview")


def calculate_compare(current, last):
    """
    Return the difference between current and last.
    Positive if current > last, negative if current < last.
    """
    return current - last


humidity_data = 73              # current
temperature_data = 18           # current
temperature_last_24h = 20       # average over last 24 hours
humidity_last_24h = 63          # average over last 24 hours
temperature_compare_24h = 20    # compares difference from temperature last 24h to current
humidity_compare_24h = 63       # compares difference from humidity last 24h to current
water_level_24h = 236


# Compute the compare values
temperature_compare_24h = calculate_compare(temperature_data, temperature_last_24h)
humidity_compare_24h    = calculate_compare(humidity_data, humidity_last_24h)


# Move to Analytics (Update 0.6 moved)
st.subheader("Last 24 hours", divider=True)
metric_24h_cols = st.columns(3)
with metric_24h_cols[0]:
    #with st.container(border=True):
    st.metric("## Temperature", f"{temperature_last_24h}°C", border=True)
with metric_24h_cols[1]:
    with st.container(border=True):
        st.metric("Humidity", F"{humidity_last_24h}%", 2)
with metric_24h_cols[2]:
    with st.container(border=True):
        st.metric("Water PH", 5, 0, delta_color="off")
with metric_24h_cols[0]:
    with st.container(border=True):
        st.metric("Water Level", f"{water_level_24h}mm", "-6mm")


cols_tools = st.columns([8, 2])
with cols_tools[0]:
    st.subheader("Temperature & Humidity", divider=True)

with cols_tools[1]:
    with st.popover(":blue[:material/help:] Graph Tools"):
        st.markdown("#### ━━━ Scroll Wheel ━━━")
        st.markdown("### :blue[:material/Mouse:]:orange[:material/unfold_more_double:] — Zoom In & Out")
        st.markdown("#### ━━ Left or Right Click ━━")
        st.markdown("### :blue[:material/Mouse:]:violet[:material/open_with:] — Move")
        # st.markdown("#### ━━━ Right Click ━━━")
        # st.markdown("### :blue[:material/Mouse:]:green[:material/swipe:] — Rotate")
        # st.markdown("### :blue[:material/Mouse:]:green[:material/swipe_vertical:] — Viewing Angle")


if os.path.exists(DATA_FILE):
    try:
        df = pd.read_csv(DATA_FILE)

        tz = timezone(timedelta(hours=8))
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d-%m-%Y, %H:%M:%S %z')
        now = datetime.now(tz)

        # Filter the DataFrame for entries within the past 24 hours
        past_24_hours = df[df['timestamp'] >= now - timedelta(hours=24)]

        # Format 'timestamp' column back to strings with desired format
        df['formatted_timestamp'] = df['timestamp'].dt.strftime('%H:%M:%S | %d-%m-%Y')

        st.line_chart(past_24_hours.set_index('timestamp')[['temperature', 'humidity']])

        latest = df.iloc[-1]

    except Exception as e:
        st.warning(f"⚠️ Unable to read or parse the CSV file: {e}")
        df = None
        latest = None

    
else:
    st.write("No data available. Please ensure the server is running and receiving data.")





