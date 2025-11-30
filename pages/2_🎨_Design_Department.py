import streamlit as st
from firebase import read, update

# ------ LOGIN CHECK -------
if "role" not in st.session_state:
    st.switch_page("login.py")

if st.session_state["role"] not in ["admin", "design"]:
    st.error("You are not allowed to access this section.")
    st.stop()

st.title("🎨 Design Department")
