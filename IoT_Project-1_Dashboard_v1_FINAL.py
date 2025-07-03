import streamlit as st
import importlib.util
import os
# from streamlit_scroll_to_top import scroll_to_here
import time
from PIL import Image
from utils import apply_css

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="IoT Hydroponics Dashboard", layout="wide", initial_sidebar_state='expanded')

# 1) Define your options
STYLE_FILES = {
    "Default": "style_default.css",
    "Dark":    "style_default_dark.css",
    "Light":   "style_default_light.css",
}

# 2) Ensure a session‐state entry exists
st.session_state.setdefault("chosen_style", "Dark")

# 3) Apply the saved CSS on page load
apply_css(STYLE_FILES[st.session_state.chosen_style])

# Anchors
st.markdown('<div id="top"></div><div id="bottom"></div>', unsafe_allow_html=True)
st.markdown('<div id="main-app2">', unsafe_allow_html=True)

# ─── Initialize Floating Containers ─────────────────────────────────────────────
#float_init()

# ─── Session State Defaults ────────────────────────────────────────────────────
st.session_state.setdefault("show_Home", False)
st.session_state.setdefault("show_Analytics", False)
st.session_state.setdefault("show_Live_Footage", False)
st.session_state.setdefault("show_System_Uptime", False)
st.session_state.setdefault("menu_selection", None)
# st.session_state.setdefault("scroll_to_bottom", False)

# ─── Callbacks ─────────────────────────────────────────────────────────────────
def select_home():
    st.session_state.menu_selection = "home_page.py"
    st.session_state.show_Analytics = False
    st.session_state.show_Live_Footage = False
    st.session_state.show_System_Uptime = False
    st.session_state.show_menu_selection = False
    # st.session_state.show_menu_features = False


def select_analytics():
    st.session_state.show_Analytics = not st.session_state.show_Analytics
    st.session_state.show_Home = False
    st.session_state.show_Live_Footage = False
    st.session_state.show_System_Uptime = False
    st.session_state.show_menu_selection = False

def select_live():
    st.session_state.show_Live_Footage = not st.session_state.show_Live_Footage
    st.session_state.show_Home = False
    st.session_state.show_Analytics = False
    st.session_state.show_System_Uptime = False
    st.session_state.show_menu_selection = False

def select_uptime():
    st.session_state.show_System_Uptime = not st.session_state.show_System_Uptime
    st.session_state.show_Home = False
    st.session_state.show_Analytics = False
    st.session_state.show_Live_Footage = False
    st.session_state.show_menu_selection = False

# Removed for Version 1.0.0 release
# def select_settings():
#     st.session_state.menu_selection = "iot_settings.py"
#     st.session_state.show_Home = False
#     st.session_state.show_Analytics = False
#     st.session_state.show_Live_Footage = False
#     st.session_state.show_System_Uptime = False

def select_features():
    st.session_state.menu_selection = "IoT_features.py"
    st.session_state.show_Home = False
    st.session_state.show_Analytics = False
    st.session_state.show_Live_Footage = False
    st.session_state.show_System_Uptime = False


def select_sub(path):
    st.session_state.menu_selection = path

# def to_bottom():
#     st.session_state.scroll_to_bottom = True


# HORIZONTAL = "image.png"
ICON = "Images/Main-Menu_White_Icon.png"

# ─── Main Content Area ─────────────────────────────────────────────────────────
with st.container():
    if st.session_state.menu_selection:
        path = st.session_state.menu_selection
        if os.path.exists(path):
            spec = importlib.util.spec_from_file_location("dynamic_module", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            #st.markdown("## No Content Found")
            st.title("No Content Found")
            st.error(f"File not found: {path}")
    else:
        select_home()
        # Rerun needed to force load home page content (on first start)
        # (NOTE-TO-SELF: Fix bug that erros home page if data from Pi is bad format)
        st.rerun()

        # st.markdown("## Welcome")
        # st.write("Select a menu or submenu to load its content.")

    #st.divider()

# ─── Sidebar Layout ────────────────────────────────────────────────────────────
with st.sidebar:

    st.logo(ICON, icon_image=ICON, size="medium")
    st.title(":blue[:material/dashboard:] IoT Hydroponics")

    # Home
    st.button(
            ":green[:material/home:] Home",
            key="btn_home",
            type="primary" if st.session_state.menu_selection=="home_page.py" else "secondary",
            on_click=select_home,
            use_container_width=True
    )

    # Analytics
    analytics_type = "primary" if st.session_state.show_Analytics else "secondary"
    st.button(
        ":orange[:material/monitoring:] Analytics",
        key="btn_analytics",
        type=analytics_type,
        on_click=select_analytics,
        use_container_width=True
    )
    if st.session_state.show_Analytics:
        st.button("• Analytics Last 24h", key="btn_analytics_opt1",
                  on_click=select_sub, args=("analytics_overview.py",))
        st.button("• Analytics Compare", key="btn_analytics_opt2",
                  on_click=select_sub, args=("analytics_details.py",))
        # st.button("Icon Browser", key="btn_icon_browser",
        #           on_click=select_sub, args=("icon_browser.py",))

    # Live Footage
    live_type = "primary" if st.session_state.show_Live_Footage else "secondary"
    st.button(
        ":violet[:material/videocam:] Live Footage",
        key="btn_live",
        type=live_type,
        on_click=select_live,
        use_container_width=True
    )
    if st.session_state.show_Live_Footage:
        st.button("• Footage List", key="btn_live_list",
                  on_click=select_sub, args=("view_footage_list.py",))
        st.button("• Footage Charts", key="btn_live_charts",
                  on_click=select_sub, args=("view_footage_charts.py",))

    # System Uptime
    uptime_type = "primary" if st.session_state.show_System_Uptime else "secondary"
    st.button(
        ":blue[:material/History:] System Uptime",
        key="btn_uptime",
        type=uptime_type,
        on_click=select_uptime,
        use_container_width=True
    )
    if st.session_state.show_System_Uptime:
        st.button("• Uptime Live", key="btn_uptime_form",
                  on_click=select_sub, args=("uptime_live.py",))
        st.button("• Uptime Review", key="btn_uptime_review",
                  on_click=select_sub, args=("uptime_stats_review.py",))
        

    st.write("") # SPACER

    main_menu_cols = st.columns([1, 3, 1])

    with main_menu_cols[1]:
        if st.button("🔄 Refresh Page", key="button_rerun"):
            st.rerun()

    st.write("")
    
    st.subheader("", divider=True)



