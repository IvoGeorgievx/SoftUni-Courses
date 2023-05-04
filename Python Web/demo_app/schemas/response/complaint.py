from marshmallow import fields

from models import State
from schemas.base_complaint import BaseComplaintSchema


class ComplaintSchemaOut(BaseComplaintSchema):
    id = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    status = fields.Enum(State, required=True)
    user_id = fields.Integer(required=True)

