from sqlalchemy_serializer import SerializerMixin
from config import db

class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'
    serialize_rules = ('-user.transactions',)

    id = db.Column(db.String(100), primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Pending")
    amount = db.Column(db.Float, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Transaction ID {self.id} Status {self.status} Amount {self.amount}>'
