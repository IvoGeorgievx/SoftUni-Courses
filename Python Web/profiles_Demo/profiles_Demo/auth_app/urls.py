from django.urls import path

from profiles_Demo.auth_app.views import SignUpView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
)