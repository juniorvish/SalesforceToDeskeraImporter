import time
from salesforce_api import get_products, get_customers, get_orders
from deskera_api import create_product, create_customer, create_order

def sync_products():
    products = get_products()
    for product in products:
        create_product(product)

def sync_customers():
    customers = get_customers()
    for customer in customers:
        create_customer(customer)

def sync_orders():
    orders = get_orders()
    for order in orders:
        create_order(order)

def sync_data():
    while True:
        sync_products()
        time.sleep(1800)
        sync_customers()
        time.sleep(1800)
        sync_orders()
        time.sleep(1800)

if __name__ == "__main__":
    sync_data()