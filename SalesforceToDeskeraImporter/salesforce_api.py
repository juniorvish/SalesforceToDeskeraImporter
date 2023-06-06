import requests
import json
from config import SALESFORCE_BASE_URL, SALESFORCE_AUTH_TOKEN

headers = {
    "Authorization": f"Bearer {SALESFORCE_AUTH_TOKEN}",
    "Content-Type": "application/json"
}

def get_all_products(filters, pagination):
    url = f"{SALESFORCE_BASE_URL}/products"
    params = {**filters, **pagination}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_all_customers(filters, pagination):
    url = f"{SALESFORCE_BASE_URL}/customers"
    params = {**filters, **pagination}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_all_orders(filters, pagination):
    url = f"{SALESFORCE_BASE_URL}/orders"
    params = {**filters, **pagination}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_all_payments(filters, pagination):
    url = f"{SALESFORCE_BASE_URL}/payments"
    params = {**filters, **pagination}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_product_details(product_id):
    url = f"{SALESFORCE_BASE_URL}/products/{product_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_customer_details(customer_id):
    url = f"{SALESFORCE_BASE_URL}/customers/{customer_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_order_details(order_id):
    url = f"{SALESFORCE_BASE_URL}/orders/{order_id}"
    response = requests.get(url, headers=headers)
    return response.json()