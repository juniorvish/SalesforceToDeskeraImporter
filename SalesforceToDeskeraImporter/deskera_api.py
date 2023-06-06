import requests
import json
from config import DESKERA_API_BASE_URL, DESKERA_AUTH_TOKEN

headers = {
    "Authorization": f"Bearer {DESKERA_AUTH_TOKEN}",
    "Content-Type": "application/json"
}

def get_products(filter_params, pagination_params):
    url = f"{DESKERA_API_BASE_URL}/products"
    params = {**filter_params, **pagination_params}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_customers(filter_params, pagination_params):
    url = f"{DESKERA_API_BASE_URL}/contacts"
    params = {**filter_params, **pagination_params}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_orders(filter_params, pagination_params):
    url = f"{DESKERA_API_BASE_URL}/sales/invoices"
    params = {**filter_params, **pagination_params}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_payments(filter_params, pagination_params):
    url = f"{DESKERA_API_BASE_URL}/payments"
    params = {**filter_params, **pagination_params}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_product_details(product_id):
    url = f"{DESKERA_API_BASE_URL}/products/{product_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_customer_details(customer_id):
    url = f"{DESKERA_API_BASE_URL}/contacts/{customer_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_order_details(order_id):
    url = f"{DESKERA_API_BASE_URL}/sales/invoices/{order_id}"
    response = requests.get(url, headers=headers)
    return response.json()