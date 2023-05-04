from marshmallow import fields

from schemas.base_user import BaseUserSchema


class UserRegisterSchemaIn(BaseUserSchema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    iban = fields.String(required=True, min_length=22, max_length=22)


class UserLoginSchema(BaseUserSchema):
    pass
