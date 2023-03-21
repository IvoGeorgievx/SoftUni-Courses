from django.urls import path

from exampreptwo.web.views import index, add_album, album_details, edit_album, delete_album, profile_details, \
    profile_delete, add_profile

urlpatterns = [
    path('', index, name='index'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('profile/add/', add_profile, name='add profile'),
]