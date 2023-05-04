import uuid

from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import auth
from models import ComplaintModel, RoleType, State, TransactionModel
from services.wise_service import WiseService


class ComplaintManager:
    @staticmethod
    def get_complaints():
        current_user = auth.current_user()
        role = current_user.role
        complaints = role_mapper[role]()
        return complaints

    @staticmethod
    def _get_complainer_complaints():
        current_user = auth.current_user()
        return ComplaintModel.query.filter_by(user_id=current_user.id).all()

    @staticmethod
    def _get_approver_complaints():
        return ComplaintModel.query.filter_by(status=State.pending).all()

    @staticmethod
    def _get_admin_complaints():
        return ComplaintModel.query.filter_by().all()

    @staticmethod
    def create_complaint(data):
        user = auth.current_user()
        data['user_id'] = user.id
        amount = data['amount']
        complaint = ComplaintModel(**data)
        db.session.add(complaint)
        db.session.flush()
        full_name = f"{user.first_name} {user.last_name}"
        iban = user.iban
        transaction = ComplaintManager.issue_transaction(amount, full_name, iban, complaint.id)

        db.session.add(transaction)
        db.session.flush()
        db.session.commit()
        return complaint

    @staticmethod
    def approve_complaint(complaint_id):
        ComplaintManager._validate_status(complaint_id)
        wise_service = WiseService()
        transfer = TransactionModel.query.filter_by(complaint_id=complaint_id).first()
        wise_service.approve_transfer(transfer.transfer_id)
        ComplaintModel.query.filter_by(id=complaint_id).update({"status": State.approved})
        db.session.commit()

    @staticmethod
    def reject_complaint(complaint_id):
        ComplaintManager._validate_status(complaint_id)
        ComplaintModel.query.filter_by(id=complaint_id).update({"status": State.rejected})
        db.session.commit()

    @staticmethod
    def delete_complaint(complaint_id):
        ComplaintModel.query.filter_by(id=complaint_id).delete()
        db.session.commit()

    @staticmethod
    def _validate_status(complaint_id):
        complaint = ComplaintModel.query.filter_by(id=complaint_id).first()
        if not complaint:
            raise BadRequest("Complaint with such ID doe not exist.")
        if complaint.status != State.pending:
            raise BadRequest("Can not change status to already processed requests")

    @staticmethod
    def issue_transaction(amount, full_name, iban, complaint_id):
        wise_service = WiseService()

        quota_id = wise_service.create_quota(amount)

        recipient_id = wise_service.create_recipient_account(full_name, iban)
        custom_transaction_id = str(uuid.uuid4())
        transaction_id = wise_service.create_transfer(quota_id, recipient_id, custom_transaction_id)
        transaction = TransactionModel(
            quote_id=quota_id,
            transfer_id=transaction_id,
            custom_transfer_id=custom_transaction_id,
            target_account_id=recipient_id,
            amount=amount,
            complaint_id=complaint_id
        )
        return transaction


role_mapper = {
    RoleType.complainer: ComplaintManager._get_complainer_complaints,
    RoleType.approver: ComplaintManager._get_approver_complaints,
    RoleType.admin: ComplaintManager._get_admin_complaints
}
