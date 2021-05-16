from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name="main-about"),
    path('data/', views.data, name="main-data"),
]
