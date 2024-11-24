# from sqlalchemy.orm import relationship
# from sqlalchemy_serializer import SerializerMixin
# from datetime import datetime, timedelta
# from config import db

# class Borrowing(db.Model, SerializerMixin):
#     __tablename__ = 'borrowings'
#     serialize_rules = ('-user.borrowings', '-book.borrowings')

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey('library_books.id'), nullable=False)
#     date_borrowed = db.Column(db.Date, nullable=False, default=datetime.utcnow)
#     due_date = db.Column(db.Date, nullable=False, default=lambda: datetime.utcnow() + timedelta(days=70))
#     date_returned = db.Column(db.Date)
#     status = db.Column(db.String, default='Pending')

#     # Relationships
#     user = relationship('User', back_populates='borrowings')
#     book = relationship('LibraryBook', back_populates='borrowings')

#     def __repr__(self):
#         return f'<Borrowing Book ID {self.book_id} by User ID {self.user_id}>'
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timedelta
from config import db

class Borrowing(db.Model, SerializerMixin):
    __tablename__ = 'borrowings'
    serialize_rules = ('-user.borrowings', '-book.borrowings', '-user.cart_items', '-book.sales')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('library_books.id'), nullable=False)
    date_borrowed = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.Date, nullable=False, default=lambda: datetime.utcnow() + timedelta(days=70))
    date_returned = db.Column(db.Date)
    status = db.Column(db.String, default='Pending')

    user = relationship('User', back_populates='borrowings')
    book = relationship('LibraryBook', back_populates='borrowings')

    def __repr__(self):
        return f'<Borrowing Book ID {self.book_id} by User ID {self.user_id}>'
