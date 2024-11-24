import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# Initialize the extensions globally but do not bind them to the app yet
db = SQLAlchemy()
bcrypt = Bcrypt()

load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_secret_key')  # Change this
    