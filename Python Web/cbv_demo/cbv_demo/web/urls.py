from django.urls import path

from cbv_demo.web.views import IndexView, IndexViewWithTemplate, IndexViewWithListView, EmployeeDetailsView, \
    EmployeeCreateView
from django.views import generic as views

urlpatterns = [
    path('', IndexViewWithListView.as_view(), name='index'),
    path('redirect-to-index/', views.RedirectView.as_view(url='/')),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='employee details'),
    path('create/', EmployeeCreateView.as_view(), name='create employee'),

]
