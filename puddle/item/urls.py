from django.urls import path

from . import views

app_name = 'item'

# Urls for this application
urlpatterns = [
    path('new/', views.new_item, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
]
