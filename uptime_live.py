# Uptime Live
import streamlit as st
import time
import os
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from utils import apply_css
import altair as alt

DATA_FILE = 'sensor_data.csv'

st.title("Uptime Live")

# 1) Define your options
STYLE_FILES = {
    "Default": "style_default.css",
    "Dark":    "style_default_dark.css",
    "Light":   "style_default_light.css", # "style_light.css",
}
# 3) Apply the saved CSS on page load
apply_css(STYLE_FILES[st.session_state.chosen_style])

# ─── Initialize Uptime ───────────────────────────────────────────────────────────
if os.path.exists(DATA_FILE):
    try:
        # Parse 'timestamp' as datetime (dayfirst=True if your date format is DD-MM-YYYY)
        df = pd.read_csv(DATA_FILE, parse_dates=['timestamp'], dayfirst=True)

        cols_select = st.columns([6, 2])

        with cols_select[0]:
            current_uptime = df.iloc[-1]['uptime'] if (df is not None and not df.empty) else 'N/A'
            st.header(f"Current Uptime - **{current_uptime}**", divider=True)

        with cols_select[1]:
            default_graph = "Default - Best for Overview"
            detailed_graph = "Detailed - Best for Detailed Analyses"
            graph_select = st.selectbox("Uptime Graphs", [default_graph, detailed_graph], 
                                index=0, placeholder="Select Graph...")
            

        with st.popover(":blue[:material/help:] Graph Tools & Tips", use_container_width=False):
            cols_pop = st.columns(2)
            with cols_pop[0]:
                st.markdown("#### ━━ Scroll Wheel ━━")
                st.markdown("### :blue[:material/Mouse:]:orange[:material/unfold_more_double:] — Zoom In & Out")
                st.markdown("#### ━ Left or Right Click ━")
                st.markdown("### :blue[:material/Mouse:]:violet[:material/open_with:] — Move")
            with cols_pop[1]:
                st.markdown("#### ━ Graph Knowledge ━")
                st.markdown("##### — Detailed Graph's lines to the left means the Flask server was off.")

        if graph_select == default_graph:

            if 'uptime' in df.columns:
                # Plot uptime against timestamp
                st.line_chart(df.set_index('uptime')['timestamp'], height=600, 
                            x_label="Uptime (Hours, Minutes, Seconds)", y_label="Start/End Time")
                
        elif graph_select == detailed_graph:
            #with st.expander("Slightly More Detailed Line Graph"):

            df['formatted_timestamp'] = df['timestamp'].dt.strftime('%H:%M:%S | \n\n%d-%m-%Y')
            # Create a base Altair chart
            base = alt.Chart(df).encode(
                x=alt.X('uptime', title='Uptime (Hours, Minutes, Seconds)'),
                y=alt.Y('timestamp', title='Start/End Time')
            )

            # Line chart
            line = base.mark_line()

            # Points with tooltips
            points = base.mark_point(color='aliceblue').encode(
                tooltip=[
                    alt.Tooltip('formatted_timestamp', title='Time')
                ]
            )

            # Combine line and points
            chart = (line + points).properties(
                height=600,
                width=700
            ).interactive()

            st.altair_chart(chart, use_container_width=True)

        else:
            st.warning("⚠️ 'uptime' column not found in the CSV data.")

    except Exception as e:
        st.warning(f"⚠️ Unable to read or parse the CSV file: {e}")
        df = None

else:
    st.write("No data available. Please ensure the server is running and receiving data.")




