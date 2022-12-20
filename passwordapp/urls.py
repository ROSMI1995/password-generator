from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView),
    path('password_display/',views.Password_display, name='password_display')
]
