from marshmallow import fields

from schemas.base_complaint import BaseComplaintSchema


class ComplaintRequestSchema(BaseComplaintSchema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    photo_url = fields.Str(required=True)
    amount = fields.Float(required=True)