from sqlalchemy.orm import validates, relationship
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
from config import db
import re

bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-password_hash', '-borrowings.user', '-sales.user', '-cart_items.user')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    profile_image = db.Column(db.String, nullable=True)

    # Relationships
    borrowings = relationship('Borrowing', back_populates='user', cascade='all, delete-orphan', lazy='joined')
    sales = relationship('Sale', back_populates='user', cascade='all, delete-orphan', lazy='joined')
    cart_items = relationship('CartItem', back_populates='user', cascade='all, delete-orphan', lazy='joined')

    @validates('email')
    def validate_email(self, key, email):
        valid_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(valid_email, email):
            raise ValueError("Invalid email")
        return email

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.name}, Email: {self.email}>'
