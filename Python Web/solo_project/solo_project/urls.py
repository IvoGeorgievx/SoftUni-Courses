
from django.contrib import admin
from django.urls import path, include

from solo_project import web_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web_app/', include('solo_project.web_app.urls'))
]
