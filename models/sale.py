from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from config import db

class Sale(db.Model, SerializerMixin):
    __tablename__ = 'sales'
    serialize_rules = ('-user.sales', '-book.sales')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('store_books.id'), nullable=False)
    date_of_sale = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default='Pending')

    # Relationships
    user = relationship('User', back_populates='sales')
    book = relationship('StoreBook', back_populates='sales')

    def __repr__(self):
        return f'<Sale Book ID {self.book_id} to User ID {self.user_id}>'
