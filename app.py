import streamlit as st
import pandas as pd
from firebase import read

# ----------- LOGIN CHECK -------------
if "role" not in st.session_state:
    st.switch_page("login.py")

role = st.session_state["role"]

st.set_page_config(page_title="OMS", layout="wide")

st.title("📦 OMS Dashboard")

st.caption(f"Logged in as: **{st.session_state['username']}**  |  Role: **{role}**")

# ----------- ADMIN ONLY --------------
if role != "admin":
    st.warning("You are not allowed to see the full dashboard.")
    st.stop()

# ----------- FETCH ORDERS -------------
orders = read("orders")

def clean_orders(data):
    if not data or not isinstance(data, dict):
        return {}
    return {k: v for k, v in data.items() if isinstance(v, dict)}

cleaned = clean_orders(orders)

if cleaned:
    df = pd.DataFrame(cleaned).T
    st.dataframe(df, use_container_width=True)
else:
    st.info("No orders found.")
