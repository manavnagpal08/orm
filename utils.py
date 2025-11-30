import uuid
from datetime import datetime

def generate_order_id():
    return "SPP" + datetime.now().strftime("%Y%m%d%H%M%S")

def today():
    return datetime.now().strftime("%d-%m-%Y")

