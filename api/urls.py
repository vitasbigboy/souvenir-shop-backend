from django.urls import path
from . import views

urlpatterns = [
    path('test-user/', views.test_user, name='test_user'),
    path('ping/', views.ping, name='ping'),
]