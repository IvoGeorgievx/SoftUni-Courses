from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.complaint import ComplaintManager
from models import RoleType
from schemas.request.complaint import ComplaintRequestSchema
from schemas.response.complaint import ComplaintSchemaOut
from utilities.decorators import validate_schema, permission_required


class ComplaintResource(Resource):
    @auth.login_required
    def get(self):
        complaints = ComplaintManager.get_complaints()
        return ComplaintSchemaOut(many=True).dump(complaints)

    @auth.login_required
    @permission_required(RoleType.complainer)
    @validate_schema(ComplaintRequestSchema)
    def post(self):
        data = request.get_json()
        complaint = ComplaintManager.create_complaint(data)
        return ComplaintSchemaOut().dump(complaint), 201


class ComplaintDeleteResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def get(self, pk):
        ComplaintManager.delete_complaint(pk)
        return None, 204


class ComplaintApproveResource(Resource):
    @auth.login_required
    @permission_required(RoleType.approver)
    def get(self, pk):
        ComplaintManager.approve_complaint(pk)


class ComplaintRejectResource(Resource):
    @auth.login_required
    @permission_required(RoleType.approver)
    def get(self, pk):
        ComplaintManager.reject_complaint(pk)
