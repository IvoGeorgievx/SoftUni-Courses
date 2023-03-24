from django.urls import path

from examprep3.web.views import index, add_book, edit_book, book_details, profile, edit_profile, delete_profile, \
    add_profile

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/add/', add_profile, name='add profile'),
    # path('add/add-book/', add_)
]


