from django.urls import path

from solo_project.web_app.views import home_page, returning_something, redirecting_showhow, supplements

urlpatterns = (
    path('', home_page, name='home page'),
    path('<int:id>/', returning_something, name='returning something'),
    path('redirecting/', redirecting_showhow, name='redirecting showhow'),
    path('home_redirect/', redirecting_showhow, name='redirect to homepage'),
    path('supplements/', supplements, name='supplements'),

)