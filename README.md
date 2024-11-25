BOOKED BACKENED API
https://booked-backend.onrender.com/

The Booked Backend API is a Flask-based RESTful service that manages an online bookstore and library system. This API handles features such as user authentication, book management, borrowing, sales, cart functionality, and payments integration.

Features
User Authentication: Secure user registration and login using hashed passwords.
Library Management: Borrow and return books, track due dates, and monitor status.
Store Management: Add books to a cart, purchase books, and manage inventory.
Payment Integration: M-Pesa payment processing with support for transaction statuses.
Admin and User Roles: Differentiate functionality between admin and regular users.
RESTful APIs: CRUD operations for books, users, transactions, and borrowings.
Cross-Origin Resource Sharing (CORS): API accessible from specified front-end clients.
Table of Contents
Technologies Used
Project Structure
Installation
Environment Variables
Usage
API Endpoints
Models
License
Technologies Used
Framework: Flask
Database: SQLite (or other SQL databases via SQLAlchemy)
ORM: SQLAlchemy
Authentication: Flask-JWT-Extended
Password Hashing: Flask-Bcrypt
Migrations: Flask-Migrate
Payment Gateway: M-Pesa API
Serialization: SQLAlchemy-Serializer
Environment Management: Python-dotenv
Project Structure
bash
Copy code
Booked-Backend/
├── models/               # Database models
├── routes/               # API routes (admin, user)
├── config.py             # Configuration settings
├── app.py                # Main application factory
├── migrations/           # Database migrations
├── .env                  # Environment variables
└── README.md             # Documentation
Installation
Prerequisites
Python 3.10+
A package manager (pip)
SQLite (or another SQL database)
Steps
Clone the repository:

bash
Copy code
git clone <https://github.com/Owiti95>/Booked-Backend.git
cd Booked-Backend
Set up a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
flask db upgrade
Create .env file and configure environment variables as specified in Environment Variables.

Run the development server:

bash
Copy code
flask run
Environment Variables
Create a .env file in the root directory with the following keys:

env
Copy code
FLASK_ENV=development
DATABASE_URL=sqlite:///booked.db
JWT_SECRET_KEY=your_jwt_secret_key
CONSUMER_KEY=your_mpesa_consumer_key
CONSUMER_SECRET=your_mpesa_consumer_secret
SHORTCODE=your_mpesa_shortcode
PASSKEY=your_mpesa_passkey
BASE_URL=https://sandbox.safaricom.co.ke
Usage
Access the API locally at http://127.0.0.1:5000.
Use tools like Postman to test the API endpoints.
API Endpoints
Admin Routes (/admin)
POST /admin/books: Add a new book to the store.
PUT /admin/books/<id>: Update book details.
DELETE /admin/books/<id>: Remove a book.
User Routes (/user)
POST /user/register: Register a new user.
POST /user/login: Authenticate a user and issue a JWT.
GET /user/cart: View items in the cart.
POST /user/cart: Add items to the cart.
POST /user/borrow: Borrow books from the library.
POST /user/pay: Process payments via M-Pesa.
Models
User
id: Integer (Primary Key)
name: String
email: String (Unique)
password_hash: String
is_admin: Boolean
Relationships: Borrowings, Sales, Cart Items
LibraryBook
id: Integer (Primary Key)
title: String
author: String
genre: String
isbn: String (Unique)
available_copies: Integer
Relationships: Borrowings
StoreBook
id: Integer (Primary Key)
title: String
author: String
genre: String
isbn: String (Unique)
price: Float
Relationships: Cart Items, Sales
Borrowing
user_id: ForeignKey to User
book_id: ForeignKey to LibraryBook
date_borrowed: Date
due_date: Date
status: String (Pending, Returned)
Sale
user_id: ForeignKey to User
book_id: ForeignKey to StoreBook
date_of_sale: Date
quantity: Integer
total_price: Float
status: String (Pending, Completed)
Transaction
id: String (Primary Key)
sale_id: ForeignKey to Sale
status: String
amount: Float
phone_number: String
License
This project is licensed under the MIT License. See the LICENSE file for details.
