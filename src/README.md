"""
Payment Processor API Documentation
================================

Overview
--------

Payment Processor is a microservice responsible for handling payment transactions.
The API provides endpoints for processing payments, retrieving payment status, and
managing user accounts.

Installation
------------

1. Clone the repository: `git clone https://github.com/your-username/payment-processor.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Run the server: `python app.py`

Endpoints
---------

### Payment Endpoints

* **POST /payments**: Create a new payment
  ```bash
  curl -X POST \
  https://example.com/payments \
  -H 'Content-Type: application/json' \
  -d '{"amount": 10.99, "currency": "USD", "user_id": 1}'
  ```
* **GET /payments/{id}**: Retrieve a payment by ID
  ```bash
  curl -X GET \
  https://example.com/payments/1
  ```
* **GET /payments/user/{id}**: Retrieve payments for a user by ID
  ```bash
  curl -X GET \
  https://example.com/payments/user/1
  ```
* **GET /users**: Retrieve all users
  ```bash
  curl -X GET \
  https://example.com/users
  ```
* **POST /users**: Create a new user
  ```bash
  curl -X POST \
  https://example.com/users \
  -H 'Content-Type: application/json' \
  -d '{"name": "John Doe", "email": "john@example.com"}'
  ```

Security
--------

* All API endpoints require authentication using a JSON Web Token (JWT) header.
* Authentication is handled using the `flask-jwt-extended` library.

Error Handling
-------------

* All API errors are returned with a 4xx status code.
* Error messages are returned in JSON format.

Models
------

* **Payment**: Represents a payment transaction
  ```python
  from dataclasses import dataclass

  @dataclass
  class Payment:
      id: int
      amount: float
      currency: str
      user_id: int
      status: str
  ```
* **User**: Represents a user account
  ```python
  from dataclasses import dataclass

  @dataclass
  class User:
      id: int
      name: str
      email: str
  ```

Requirements
------------

* `flask`: The Flask web framework
* `flask-jwt-extended`: JWT authentication library
* `pyjwt`: JWT library
* `requests`: HTTP library