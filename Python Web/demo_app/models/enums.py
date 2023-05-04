import enum


class RoleType(enum.Enum):
    complainer = 'complainer'
    approver = 'approver'
    admin = 'admin'


class State(enum.Enum):
    pending = 'pending'
    approved = 'approved'
    rejected = 'rejected'
