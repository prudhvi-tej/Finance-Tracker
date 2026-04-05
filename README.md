# Finance Tracker Backend

## Overview

This project is a backend finance tracking system built using Django and Django REST Framework. It allows users to manage financial transactions (income and expenses) and provides analytical insights such as total income, expenses, and balance.

## Tech Stack

* Django
* Django REST Framework
* PostgreSQL
* Django ORM

## Features

* CRUD operations for financial transactions
* Filtering by type, category, and date
* Search functionality
* Pagination support
* Analytics:

  * Total income
  * Total expenses
  * Balance
  * Category-wise breakdown
  * Monthly summary
  * Recent transactions
* Role-based access control (Viewer, Analyst, Admin)

## Setup Instructions

1. Clone the repository:
   git clone <repo-link>

2. Navigate to project folder:
   cd finance-tracker-backend

3. Install dependencies:
   pip install -r requirements.txt

4. Configure PostgreSQL database in settings.py

5. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

6. Start the server:
   python manage.py runserver

## API Endpoints

### Transactions

* GET /api/transactions/
* POST /api/transactions/
* PUT /api/transactions/{id}/
* DELETE /api/transactions/{id}/

### Filters & Search

* /api/transactions/?type=income
* /api/transactions/?category=food
* /api/transactions/?search=salary

### Analytics

* /api/summary/
* /api/category-summary/
* /api/monthly-summary/
* /api/recent/


## Assumptions

* Each transaction belongs to a user
* Amount must be positive
* Basic role-based access implemented 

## How to Test

* Use browser or Postman to test API endpoints
* Visit /api/transactions/ for CRUD operations
* Visit /api/summary/ for analytics

