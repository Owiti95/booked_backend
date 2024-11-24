
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp
from models import db
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load config from config.py

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app, origins=["http://localhost:5173", "https://booked-client.vercel.app"], supports_credentials=True)

        # M-Pesa configuration
    app.config["CONSUMER_KEY"] = os.getenv("CONSUMER_KEY")
    app.config["CONSUMER_SECRET"] = os.getenv("CONSUMER_SECRET")
    app.config["SHORTCODE"] = os.getenv("SHORTCODE")
    app.config["PASSKEY"] = os.getenv("PASSKEY")
    app.config["BASE_URL"] = os.getenv("BASE_URL")

    # Register Blueprints
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
