# from sqlalchemy.orm import relationship
# from sqlalchemy_serializer import SerializerMixin
# from config import db

# class CartItem(db.Model, SerializerMixin):
#     __tablename__ = 'cart_items'
#     serialize_rules = ('-user.cart_items', '-book.cart_items')

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey('store_books.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)

#     # Relationships
#     user = relationship('User', back_populates='cart_items')
#     book = relationship('StoreBook', back_populates='cart_items')

#     def __repr__(self):
#         return f'<CartItem User ID {self.user_id} Book ID {self.book_id} Quantity {self.quantity}>'
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from config import db

class CartItem(db.Model, SerializerMixin):
    __tablename__ = 'cart_items'
    serialize_rules = ('-user.cart_items', '-book.cart_items', '-user.borrowings', '-book.sales')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('store_books.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    user = relationship('User', back_populates='cart_items')
    book = relationship('StoreBook', back_populates='cart_items')

    def __repr__(self):
        return f'<CartItem User ID {self.user_id} Book ID {self.book_id} Quantity {self.quantity}>'
