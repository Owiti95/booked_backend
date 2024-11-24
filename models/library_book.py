# from sqlalchemy.orm import relationship
# from sqlalchemy_serializer import SerializerMixin
# from config import db

# class LibraryBook(db.Model, SerializerMixin):
#     __tablename__ = 'library_books'
#     serialize_rules = ('-borrowings.book',)

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     author = db.Column(db.String, nullable=False)
#     genre = db.Column(db.String, nullable=False)
#     isbn = db.Column(db.String, unique=True, nullable=False)
#     available_copies = db.Column(db.Integer, default=0)
#     total_copies = db.Column(db.Integer, default=0)
#     image_url = db.Column(db.String, nullable=True)

#     # Relationships
#     borrowings = relationship('Borrowing', back_populates='book', cascade='all, delete-orphan', lazy='joined')

#     def __repr__(self):
#         return f'<LibraryBook {self.title} by {self.author}>'
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from config import db

class LibraryBook(db.Model, SerializerMixin):
    __tablename__ = 'library_books'
    serialize_rules = ('-borrowings.book', '-borrowings.user.borrowings')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    isbn = db.Column(db.String, unique=True, nullable=False)
    available_copies = db.Column(db.Integer, default=0)
    total_copies = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String, nullable=True)

    borrowings = relationship('Borrowing', back_populates='book', cascade='all, delete-orphan', lazy='select')

    def __repr__(self):
        return f'<LibraryBook {self.title} by {self.author}>'
