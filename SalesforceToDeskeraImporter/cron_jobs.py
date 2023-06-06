import schedule
import time
from sync import sync_products, sync_customers, sync_orders

def job_sync_products():
    sync_products()

def job_sync_customers():
    sync_customers()

def job_sync_orders():
    sync_orders()

schedule.every(30).minutes.do(job_sync_products)
schedule.every(30).minutes.do(job_sync_customers)
schedule.every(30).minutes.do(job_sync_orders)

while True:
    schedule.run_pending()
    time.sleep(1)