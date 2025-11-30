import streamlit as st
from firebase import read, update

st.title("🎨 Design Department")

orders = read("orders")

if not orders:
    st.info("No orders available.")
else:
    for key, order in orders.items():
        if order["stage"] == "Design":
            st.subheader(f"Order: {order['order_id']} - {order['customer']}")

            assign = st.text_input(f"Assigned To ({order['order_id']})")
            ref_upload = st.file_uploader("Reference Design")
            template = st.selectbox("Template Used", ["SEPA", "Digital", "Brand Design"])
            start = st.button(f"Start {order['order_id']}")
            complete = st.button(f"Complete {order['order_id']}")

            if complete:
                update(f"orders/{key}", {"stage": "Printing"})
                st.success("Moved to Printing Department")
                st.experimental_rerun()

