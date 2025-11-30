import streamlit as st
from firebase import read, update

st.title("🎨 Design Department")

orders = read("orders")

if not orders or not isinstance(orders, dict):
    st.info("No valid orders available.")
else:
    found = False
    for key, order in orders.items():
        if not isinstance(order, dict):
            continue

        if order.get("stage") == "Design":
            found = True
            st.subheader(f"Order: {order['order_id']} - {order['customer']}")

            assign = st.text_input(f"Assigned To ({order['order_id']})")
            ref_upload = st.file_uploader("Reference Design")
            template = st.selectbox("Template Used", ["SEPA", "Digital", "Brand Design"])

            if st.button(f"Complete {order['order_id']}"):
                update(f"orders/{key}", {"stage": "Printing"})
                st.success("Moved to Printing Department")
                st.experimental_rerun()

    if not found:
        st.info("No orders currently in Design stage.")
