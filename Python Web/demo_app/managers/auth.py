from datetime import datetime, timedelta

import jwt
from flask import request
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest, Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.user import User


class AuthManager:
    @staticmethod
    def register(data):
        data = request.get_json()
        data['password'] = generate_password_hash(data['password'], method='sha256')
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login_user(data):
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            raise BadRequest("Invalid email or password")

        if not check_password_hash(user.password, data['password']):
            raise BadRequest("invalid email or password")

        return user

    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=2)
        }
        return jwt.encode(payload, key='123', algorithm='HS256')

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(token, key='123', algorithms=['HS256'])
        except Exception as ex:
            # fix this
            raise BadRequest("Invalid or expired token")


auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    try:
        payload = AuthManager.decode_token(token)
        user = User.query.filter_by(id=payload['sub']).first()
        if not user:
            raise Unauthorized("invalid or missing token")
        return user
    except Exception as ex:
        raise Unauthorized("invalid or missing token")
