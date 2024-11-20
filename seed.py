from app import create_app
from config import db
from models import User, StoreBook, LibraryBook, CartItem, Borrowing
from datetime import datetime, timedelta
import cloudinary.uploader
import os

import cloudinary
from my_cloudinary_config import Cloudinary_config

cloudinary.config(
    cloud_name=Cloudinary_config["CLOUD_NAME"],
    api_key=Cloudinary_config["API_KEY"],
    api_secret=Cloudinary_config["API_SECRET"]
)

app = create_app()  # Initialize the app

# Create tables
with app.app_context():
    db.create_all()

# Helper function to upload image to Cloudinary
def upload_to_cloudinary(image_path):
    if not os.path.exists(image_path):
        print(f"Image file does not exist: {image_path}")
        return None
    try:
        response = cloudinary.uploader.upload(image_path)
        return response.get('secure_url')  # Return the secure URL
    except Exception as e:
        print(f"Error uploading {image_path} to Cloudinary: {e}")
        return None

# Run the seeding process
def seed_data():
    try:
        # Delete existing data before seeding
        db.session.query(User).delete()
        db.session.commit()

        # Add sample books for the store
        store_books_data = [
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction', 'isbn': '1234567890', 'price': 15.99, 'stock': 20, 'image_path': './images/gatsby.jpg'},
            {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'genre': 'Non-Fiction', 'isbn': '0987654321', 'price': 20.99, 'stock': 15, 'image_path': './images/sapiens.jpg'},
            # Add remaining books here...
        ]

        store_books = []
        for book_data in store_books_data:
            image_url = upload_to_cloudinary(book_data.pop('image_path'))
            if image_url:
                store_books.append(StoreBook(image_url=image_url, **book_data))

        # Add sample library books
        library_books_data = [
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction', 'isbn': '1122334455', 'available_copies': 5, 'total_copies': 10, 'image_path': './images/mockingbird.jpg'},
            {'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'genre': 'Science', 'isbn': '5566778899', 'available_copies': 2, 'total_copies': 4, 'image_path': './images/brief_history.jpg'},
            # Add remaining library books here...
        ]

        library_books = []
        for book_data in library_books_data:
            image_url = upload_to_cloudinary(book_data.pop('image_path'))
            if image_url:
                library_books.append(LibraryBook(image_url=image_url, **book_data))

        # Add users with unique emails
        users = [
            User(name='Alice Johnson', email='alice@example.com', is_admin=False),
            User(name='Admin User', email='admin@example.com', is_admin=True),
            User(name='Bob Smith', email='bob@example.com', is_admin=False),  # Unique email
            # Add remaining users here...
        ]

        # Set passwords for users
        for user in users:
            user.set_password('defaultpassword123')

        # Commit base records
        db.session.add_all(store_books + library_books + users)
        db.session.commit()

        print("Database seeded successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding data: {e}")
    finally:
        db.session.close()

# Run the seeding function
if __name__ == "__main__":
    with app.app_context():
        seed_data()