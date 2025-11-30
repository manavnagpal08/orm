import streamlit as st
from firebase import read
import pandas as pd

st.set_page_config(page_title="OMS - Order Management System", layout="wide")

st.title("📦 Order Management System")
st.write("Track orders across Design → Printing → DieCut → Assembly → Dispatch")

orders = read("orders")

if orders:
    df = pd.DataFrame(orders).T
    st.dataframe(df)
else:
    st.info("No orders found.")

