import streamlit as st
import pandas as pd
from firebase import read

st.set_page_config(
    page_title="OMS - Order Management System",
    layout="wide"
)

st.title("📦 Order Management System")
st.caption("Track orders across Design → Printing → Die-Cut → Assembly → Dispatch")

# -----------------------------
# FETCH ORDERS FROM FIREBASE
# -----------------------------
orders = read("orders")

# -----------------------------
# VALIDATION & CLEANING LOGIC
# -----------------------------
def clean_orders(data):
    """
    Firebase sometimes returns corrupted nodes:
    strings, numbers, or empty values.
    This function filters to keep only valid dictionaries.
    """
    if not data or not isinstance(data, dict):
        return {}

    clean = {}
    for key, value in data.items():
        if isinstance(value, dict):     # Valid order
            clean[key] = value

    return clean


cleaned = clean_orders(orders)

# -----------------------------
# DISPLAY ORDERS
# -----------------------------
if cleaned:
    try:
        df = pd.DataFrame(cleaned).T

        # Sorting by latest order (if order_id exists)
        if "order_id" in df.columns:
            df = df.sort_values("order_id", ascending=False)

        st.subheader("📋 All Orders")
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error displaying orders: {e}")
        st.write("Raw Firebase data:", orders)

else:
    st.info("No orders found. Create your first order from the sidebar pages!")

# -----------------------------
# FOOTER
# -----------------------------
with st.expander("🔧 Debug Info (click to expand)"):
    st.write("Raw Firebase Data:", orders)
