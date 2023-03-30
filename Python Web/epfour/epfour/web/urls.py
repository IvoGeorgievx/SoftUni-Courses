from django.urls import path

from epfour.web.views import index, add_note, edit_note, delete_note, details_note, profile, create_profile

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
    path('profile/', profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
]