import streamlit as st
from firebase import push
from utils import generate_order_id, today

st.title("📦 Create New Order")

order_id = generate_order_id()
st.text_input("Order ID", order_id, disabled=True)

customer = st.text_input("Customer Name")
item = st.text_area("Item / Product Description")
qty = st.number_input("Quantity", min_value=1)
receive_date = st.date_input("Order Received Date")
due_date = st.date_input("Due Date")

st.subheader("Additional Settings")
new_or_repeat = st.selectbox("Order Type", ["New", "Repeat"])
advance = st.radio("Advance Received?", ["Yes", "No"])
foil = st.text_input("Foil Printing ID")
spotuv = st.text_input("Spot UV ID")
brand_thickness = st.text_input("Brand Quality & Thickness ID")
paper_thickness = st.text_input("Paper Quality & Thickness ID")
size = st.text_input("Size ID")
rate = st.number_input("Rate", min_value=0.0)

if st.button("Create Order"):
    data = {
        "order_id": order_id,
        "customer": customer,
        "item": item,
        "qty": qty,
        "received": str(receive_date),
        "due": str(due_date),
        "new_or_repeat": new_or_repeat,
        "advance": advance,
        "foil_id": foil,
        "spotuv_id": spotuv,
        "brand_thickness_id": brand_thickness,
        "paper_thickness_id": paper_thickness,
        "size_id": size,
        "rate": rate,
        "stage": "Design"
    }
    push("orders", data)
    st.success("Order Created Successfully!")
