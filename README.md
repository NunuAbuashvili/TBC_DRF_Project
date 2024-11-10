# Chocolate Shop E-commerce Platform

## Overview

A Django-based e-commerce platform specialized in chocolate products, built with Django Rest Framework. 
This project is currently in the initial stage and will be expanded over time with more features.

## Features

- **Product Management**
    - Dynamic product catalog with detailed product pages.
    - Category-based product organization.
- **Class-based Views**


## Project Structure

### Apps
- `account`: Handles custom user implementation.
- `order`: Manages shopping cart.
    - Models: Cart, CartItem
- `store`: Manages products and categories.
    - Models: Product, Category, Tag
- `api`: Manages DRF APIs.
- `main`: Handles main page functionality.


### API Endpoints

### Api
- `/products`: A list of all available products.
- `/product/<int:pk>`: Product detail page.
- `/categories`: A list of all categories.
- `/category/<slug:slug>`: Category detail page.


## Setup

1. Clone the repository.
2. Install the required packages:
    ```bash
   pip install -r requirements.txt
3. Run migrations: 
    ```bash
    python manage.py migrate
4. Create a superuser for accessing the admin panel: 
   ```bash
   python manage.py createsuperuser
5. Run the development server: 
   ```bash
   python manage.py runserver


## Contributing
This project is part of a learning process. While contributions are welcome, 
please note that major changes may be implemented as part of the learning journey.


## Note
This README is in its initial state and will be updated regularly as the project evolves. 
Check back for the latest information on features and usage.

*Last updated: [10.11.2024]*