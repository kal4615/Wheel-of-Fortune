from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('play/', views.play_page, name='play'),
]