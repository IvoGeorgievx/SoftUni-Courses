from django.contrib import admin
from django.urls import path, include

from exam_first_prep.gamesplay_app.views import create_profile, home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam_first_prep.gamesplay_app.urls')),
]
