# SalesforceToDeskeraImporter

This project is an import tool to import data from Salesforce to Deskera. It provides APIs and cron jobs to sync products, customers, and orders between the two platforms.

## Getting Started

To get started, clone the repository:

```
git clone https://github.com/juniorvish/SalesforceToDeskeraImporter.git
```

## Installation

1. Install the required dependencies:

```
npm install
```

2. Create a `.env` file in the root directory and add the following variables:

```
SALESFORCE_AUTH_TOKEN=<your_salesforce_auth_token>
DESKERA_AUTH_TOKEN=<your_deskera_auth_token>
```

Replace `<your_salesforce_auth_token>` and `<your_deskera_auth_token>` with your respective API tokens.

## Running the Project

1. Start the server:

```
npm start
```

2. The APIs and cron jobs will now be running. The cron jobs will sync data between Salesforce and Deskera every 30 minutes.

## API Endpoints

- `GET /api/products`: Get all products with filters and pagination
- `GET /api/customers`: Get all customers with filters and pagination
- `GET /api/orders`: Get all orders with filters and pagination
- `GET /api/payments`: Get all payments against orders with filters and pagination
- `GET /api/products/:id`: Get details on a product by id
- `GET /api/customers/:id`: Get details on a customer by id
- `GET /api/orders/:id`: Get details on an order by id

## Cron Jobs

- `syncProducts`: Sync newly created products from Salesforce to Deskera every 30 minutes
- `syncCustomers`: Sync newly created customers from Salesforce to Deskera every 30 minutes
- `syncOrders`: Sync newly created orders from Salesforce to Deskera every 30 minutes