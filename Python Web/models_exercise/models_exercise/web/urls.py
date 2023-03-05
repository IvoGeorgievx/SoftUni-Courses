from django.urls import path

from models_exercise.web.views import index

urlpatterns = (
    path('', index, name='index'),
)