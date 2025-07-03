# home_page_1
import streamlit as st
#from utils import apply_css
import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
import os
import threading


DATA_FILE = 'sensor_data.csv'


# Initialize session state for warning dismissal
if 'dismiss_warning' not in st.session_state:
    st.session_state['dismiss_warning'] = False

# Define spike thresholds
TEMP_HIGH_THRESHOLD = 35.0  # degrees Celsius (45)
TEMP_LOW_THRESHOLD = 4.0  # data updates every 60 seconds ( debug was 10s )
TEMP_SPIKE_THRESHOLD = 2.0  
HUMIDITY_SPIKE_THRESHOLD = 10.0  # percentage
HUMIDITY_LOW_THRESHOLD = 40.0


# st.session_state.formatted_time = time.strftime("%I:%M %p", time.localtime())
# %I → Hour (01–12) %H → Hour (00–23) %M → Minute (00–59) %S → Second (00–59) %p → Locale’s AM or PM


st.title("Hydroponics Overview")



def calculate_compare(current, last):
    """
    Return the difference between current and last.
    Positive if current > last, negative if current < last.
    """
    return current - last

# Test Data - Debugging
humidity_data = 73              # current
temperature_data = 18           # current
temperature_last_24h = 20       # average over last 24 hours
humidity_last_24h = 63          # average over last 24 hours
temperature_compare_24h = 20    # compares difference from temperature last 24h to current
humidity_compare_24h = 63       # compares difference from humidity last 24h to current


# Compute the compare values
temperature_compare_24h = calculate_compare(temperature_data, temperature_last_24h)
humidity_compare_24h    = calculate_compare(humidity_data, humidity_last_24h)

main_cols = st.columns([1, 2])


with main_cols[1]:

    cols_tools = st.columns([8, 2])
    with cols_tools[0]:
        st.subheader("Sensors: Temperature & Humidity (Last 24 Hours)", divider=True)

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
            df['timestamp'] = pd.to_datetime(df['timestamp'], format='%H:%M:%S, %d-%m-%Y %z')
            now = datetime.now(tz)

            # Filter the DataFrame for entries within the past 24 hours
            past_24_hours = df[df['timestamp'] >= now - timedelta(hours=24)]

            # Format 'timestamp' column back to strings with desired format
            df['formatted_timestamp'] = df['timestamp'].dt.strftime('%H:%M:%S | %d-%m-%Y')
            # df['formatted_timestamp_graph'] = df['timestamp'].dt.strftime('%H:%M:%S | %d-%m-%Y')

            # Insert colon into timezone offset
            # df['formatted_timestamp'] = df['formatted_timestamp'].str.replace(
            #     r'(\+|\-)(\d{2})(\d{2})$', r'\1\2:\3', regex=True
            # )

            st.line_chart(past_24_hours.set_index('timestamp')[['temperature', 'humidity']])

            latest = df.iloc[-1]
            # st.write(f"Timestamp: {latest['timestamp']}")
            # st.write(f"Temperature: {latest['temperature']} °C")
            # st.write(f"Humidity: {latest['humidity']} %")

        except Exception as e:
            st.warning(f"⚠️ Unable to read or parse the CSV file: {e}")
            st.info("Check if data is in the CSV file.")
            df = None
            latest = None

        
    else:
        st.write("No data available. Please ensure the server is running and receiving data.")



with main_cols[0]:
    # st.subheader(f"Current Stats: {latest['formatted_timestamp']}", divider=True)
    
    try:
        st.subheader(f"Current Stats: {latest['formatted_timestamp']}")
    
        metric_current_cols = st.columns(2)

        with metric_current_cols[0]:
            st.metric("Temperature",
                    f"{latest['temperature']} °C",
                    f"{temperature_compare_24h:+d}", border=True)

        with metric_current_cols[1]:
            with st.container(border=True):
                st.metric("Humidity", f"{latest['humidity']} %", 2)

    except Exception as e:
        st.warning(f"⚠️ Unable to read or parse the CSV file: {e}")
        df = None
        latest = None




with main_cols[0]:
    st.subheader("Alarms", divider=True)

    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)

            # Ensure there are at least two readings to compare
            if len(df) >= 2:
                latest = df.iloc[-1]
                previous = df.iloc[-2]

                # Calculate differences
                temp_diff = abs(latest['temperature'] - previous['temperature'])
                humidity_diff = abs(latest['humidity'] - previous['humidity'])

                # Initialize warning messages list
                warning_messages = []

                # Check for temperature thresholds
            if latest['temperature'] > TEMP_HIGH_THRESHOLD:
                warning_messages.append(f"High Temperature Alert: {latest['temperature']}°C exceeds {TEMP_HIGH_THRESHOLD}°C threshold at {latest['timestamp']}.")
            elif latest['temperature'] < TEMP_LOW_THRESHOLD:
                warning_messages.append(f"Low Temperature Alert: {latest['temperature']}°C is below {TEMP_LOW_THRESHOLD}°C threshold at {latest['timestamp']}.")

            # Check for humidity threshold
            if latest['humidity'] < HUMIDITY_LOW_THRESHOLD:
                warning_messages.append(f"Low Humidity Alert: {latest['humidity']}% is below {HUMIDITY_LOW_THRESHOLD}% threshold at {latest['timestamp']}.")

            # Check for temperature spike
            if temp_diff > TEMP_SPIKE_THRESHOLD:
                spike_time_temp = previous['timestamp']
                warning_messages.append(f"Temperature Spike Detected: Change of {temp_diff:.2f}°C at {spike_time_temp}.")

            # Check for humidity spike
            if humidity_diff > HUMIDITY_SPIKE_THRESHOLD:
                spike_time_hum = previous['timestamp']
                warning_messages.append(f"Humidity Spike Detected: Change of {humidity_diff:.2f}% at {spike_time_hum}.")

            # Display warnings if any and not dismissed
            if warning_messages and not st.session_state.dismiss_warning:
                for message in warning_messages:
                    st.warning(f"⚠️ {message}")
                if st.checkbox("Dismiss warnings"):
                    st.session_state.dismiss_warning = True

        except Exception as e:
            st.warning(f"⚠️ Unable to read or parse the CSV file: {e}")
    else:
        st.write("No data available. Please ensure the server is running and receiving data.")



# Auto Refresh Script (W.I.P)
# with main_cols[1]:

# # Function to be called after the countdown
# def trigger_rerun():
#     st.session_state['countdown_active'] = False
#     st.rerun()

# # Initialize session state variables
# if 'countdown_active' not in st.session_state:
#     st.session_state['countdown_active'] = False

# # Start the countdown automatically if not already active
# if not st.session_state['countdown_active']:
#     st.session_state['countdown_active'] = True
#     countdown_seconds = 10  # Set your desired countdown duration here
#     timer = threading.Timer(countdown_seconds, trigger_rerun)
#     timer.start()
#     st.success(f"Countdown started for {countdown_seconds} seconds.")

# # Display countdown status
# if st.session_state['countdown_active']:
#     st.info("Countdown in progress... The page will rerun shortly.")
# else:
#     st.info("Countdown completed.")