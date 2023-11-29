from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

# Urls for this application
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
