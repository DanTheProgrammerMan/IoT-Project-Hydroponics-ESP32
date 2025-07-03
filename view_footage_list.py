# home_page_1
import streamlit as st
#from utils import apply_css

st.title("Live Footage List")

# Placeholders
cols_list = st.columns(3)

with cols_list[0]:
    st.subheader("Camera 1 - Graden Bed", divider=True)
    st.image("Images/footage_placeholder_1.jpg", caption="PLACEHOLDER 1", 
             use_container_width=True)

with cols_list[1]:
    st.subheader("Camera 2 - Graden Bed 2", divider=True)
    st.image("Images/footage_placeholder_2.jpg", caption="PLACEHOLDER 2",  
             use_container_width=True)

with cols_list[2]:
    st.subheader("Camera 3 - Plant 1", divider=True)
    st.image("Images/footage_placeholder_3.jpg", caption="PLACEHOLDER 3",  
             use_container_width=True)




