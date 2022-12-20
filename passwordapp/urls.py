from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView),
    path('password/',views.Password_display)
]
