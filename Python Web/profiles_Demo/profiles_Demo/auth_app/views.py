from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from profiles_Demo.auth_app.forms import SignUpForm


# Create your views here.
class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('sign up')
