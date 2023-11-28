from django.urls import path

from . import views

app_name = 'dashboard'

# Urls for this application
urlpatterns = [
    path('', views.index, name='index'),
]
