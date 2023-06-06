import os

# Salesforce API configuration
SALESFORCE_API_BASE_URL = os.environ.get("SALESFORCE_API_BASE_URL", "https://your_salesforce_instance_url")
SALESFORCE_CLIENT_ID = os.environ.get("SALESFORCE_CLIENT_ID", "your_salesforce_client_id")
SALESFORCE_CLIENT_SECRET = os.environ.get("SALESFORCE_CLIENT_SECRET", "your_salesforce_client_secret")
SALESFORCE_USERNAME = os.environ.get("SALESFORCE_USERNAME", "your_salesforce_username")
SALESFORCE_PASSWORD = os.environ.get("SALESFORCE_PASSWORD", "your_salesforce_password")
SALESFORCE_SECURITY_TOKEN = os.environ.get("SALESFORCE_SECURITY_TOKEN", "your_salesforce_security_token")

# Deskera API configuration
DESKERA_API_BASE_URL = os.environ.get("DESKERA_API_BASE_URL", "https://api.deskera.com")
DESKERA_AUTH_TOKEN = os.environ.get("DESKERA_AUTH_TOKEN", "your_deskera_auth_token")

# Sync intervals (in seconds)
SYNC_PRODUCTS_INTERVAL = 30 * 60  # 30 minutes
SYNC_CUSTOMERS_INTERVAL = 30 * 60  # 30 minutes
SYNC_ORDERS_INTERVAL = 30 * 60  # 30 minutes