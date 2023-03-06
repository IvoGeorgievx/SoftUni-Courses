from django.urls import path

from html_demo.web.views import index, index1

urlpatterns = (
    path('', index, name='index'),
    path('1/', index1, name='index1'),
)