from django.urls import path

from . import views

app_name = 'item'

# Urls for this application
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]
