the app is: SalesforceToDeskeraImporter

the files we have decided to generate are: 
1. api/auth.js
2. api/products.js
3. api/customers.js
4. api/orders.js
5. api/payments.js
6. cron/syncProducts.js
7. cron/syncCustomers.js
8. cron/syncOrders.js
9. README.md

Shared dependencies:
1. authToken: Authorization token for API requests
2. getProducts: Function to get all products with filters and pagination
3. getCustomers: Function to get all customers with filters and pagination
4. getOrders: Function to get all orders with filters and pagination
5. getPayments: Function to get all payments against orders with filters and pagination
6. getProductDetails: Function to get details on a product by id
7. getCustomerDetails: Function to get details on a customer by id
8. getOrderDetails: Function to get details on an order by id
9. syncProducts: Function to sync newly created products from Salesforce to Deskera
10. syncCustomers: Function to sync newly created customers from Salesforce to Deskera
11. syncOrders: Function to sync newly created orders from Salesforce to Deskera
12. filterParams: Object containing filter parameters for API requests (created date, updated date, name, code)
13. paginationParams: Object containing pagination parameters for API requests (page, limit)
14. idNames: Object containing id names for DOM elements used by JavaScript functions (if applicable)
15. messageNames: Object containing message names for communication between components (if applicable)