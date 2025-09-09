# Grocery Shopping Application

A web-based grocery store platform built with Flask and SQLAlchemy.

### Problem Statement

Design and implement a dynamic grocery store web application that enables:
- Admins to manage inventory and categories.
- Customers to browse, search, and purchase products online.
- Secure user authentication and role-based access to application features.
- Real-time order and cart management with proper inventory updates and historical record keeping.

## Features

- **Admin Dashboard:** Add, edit, and delete product categories and products.
- **User Authentication:** Registration, login, and profile management for admins and customers.
- **Product Browsing:** Search and filter products by category, name, and price.
- **Shopping Cart:** Add products to cart, update quantities, and remove items.
- **Order Management:** Place orders, adjust stock quantities, and view past orders.
- **CSV Export:** Download order history as a CSV file.
- **Role-Based Access:** Separate admin and customer functionalities for secure access.

## Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy (ORM)
- SQLite (default)
- Jinja2 templating

## Setup Instructions

1. Clone this repository:
    ```
    git clone https://github.com/vikas-06978/grocery.git
    ```
2. Install requirements:
    ```
    pip install -r requirements.txt
    ```
3. Run the application:
    ```
    python app.py
    ```
4. Open `http://localhost:5000` in your browser.

## Folder Structure

- `models.py`: Database models for users, categories, products, carts, transactions, orders.
- `routes.py`: Application routes for authentication, admin actions, product management, shopping cart, orders, and exporting data.
- `templates/`: HTML templates for all views (admin, cart, profile, orders, etc.).
- `static/`: Static assets (e.g., exported CSV files).
- `config.py`: Configuration (not shown here; add as needed).
- `api.py`: API endpoints (implement as required).

## Usage

- Register as a new user (customer).
- Admin access is created automatically with username `admin` and password `admin`.
- Customers can browse products, add to cart, and place orders.
- Admins can manage categories and products.

## License

This project is licensed under the MIT License, © 2024 Vikas-06978.

**Copyright (c) 2024 Vikas-06978**  
Licensed under the MIT License  
