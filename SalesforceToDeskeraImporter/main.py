import sys
from salesforce_api import getProducts, getCustomers, getOrders, getPayments, getProductDetails, getCustomerDetails, getOrderDetails
from deskera_api import syncProducts, syncCustomers, syncOrders
from cron_jobs import startCronJobs

def main():
    try:
        startCronJobs(syncProducts, syncCustomers, syncOrders)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()