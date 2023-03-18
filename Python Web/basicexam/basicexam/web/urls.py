from django.urls import path

from basicexam.web.views import index, catalogue, create_profile, car_create, car_details, car_edit, car_delete, \
    profile_details, edit_profile, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/create/', create_profile, name='create profile'),
    path('car/create/', car_create, name='car create'),
    path('car/<int:pk>/details/', car_details, name='car details'),
    path('car/<int:pk>/edit/', car_edit, name='car edit'),
    path('car/<int:pk>/delete/', car_delete, name='car delete'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

]
