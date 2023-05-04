from db import db
from models.enums import RoleType


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.complainer,
        nullable=False
    )
    iban = db.Column(db.String(22))





