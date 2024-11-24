# from sqlalchemy.orm import relationship
# from sqlalchemy_serializer import SerializerMixin
# from config import db

# class StoreBook(db.Model, SerializerMixin):
#     __tablename__ = 'store_books'
#     serialize_rules = ('-cart_items.book', '-sales.book')

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     author = db.Column(db.String, nullable=False)
#     genre = db.Column(db.String, nullable=False)
#     isbn = db.Column(db.String, unique=True, nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     stock = db.Column(db.Integer, default=0)
#     image_url = db.Column(db.String, nullable=True)

#     # Relationships
#     cart_items = relationship('CartItem', back_populates='book', cascade='all, delete-orphan', lazy='joined')
#     sales = relationship('Sale', back_populates='book', cascade='all, delete-orphan', lazy='joined')

#     def __repr__(self):
#         return f'<StoreBook {self.title} by {self.author}>'
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from config import db

class StoreBook(db.Model, SerializerMixin):
    __tablename__ = 'store_books'
    serialize_rules = ('-cart_items.book', '-sales.book', '-cart_items.user.cart_items', '-sales.user.sales')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    isbn = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String, nullable=True)

    cart_items = relationship('CartItem', back_populates='book', cascade='all, delete-orphan', lazy='select')
    sales = relationship('Sale', back_populates='book', cascade='all, delete-orphan', lazy='select')

    def __repr__(self):
        return f'<StoreBook {self.title} by {self.author}>'
