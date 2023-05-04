from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from schemas.request.users import UserRegisterSchemaIn, UserLoginSchema
from schemas.response.users import UserAuthResponseSchema
from utilities.decorators import validate_schema


class SignUp(Resource):
    @validate_schema(UserRegisterSchemaIn)
    def post(self):
        data = request.get_json()
        user = AuthManager.register(data)
        token = AuthManager.encode_token(user)
        return UserAuthResponseSchema().dump({"token": token})


class LoginResource(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        user = AuthManager.login_user(data)
        token = AuthManager.encode_token(user)
        return UserAuthResponseSchema().dump({"token": token})




