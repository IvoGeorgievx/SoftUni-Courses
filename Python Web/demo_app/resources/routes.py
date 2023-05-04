from resources.auth import LoginResource, SignUp
from resources.complaint import ComplaintResource, ComplaintRejectResource, \
    ComplaintApproveResource, ComplaintDeleteResource

routes = (
    (SignUp, '/register'),
    (LoginResource, '/login'),
    (ComplaintResource, '/complaints'),
    (ComplaintApproveResource, '/complaints/<int:pk>/approve'),
    (ComplaintRejectResource, '/complaints/<int:pk>/reject'),
    (ComplaintDeleteResource, '/complaints/<int:pk>/delete'),
)
