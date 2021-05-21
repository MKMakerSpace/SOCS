from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name="main-about"),
    path('data/', views.data, name="main-data"),
    path('admin/', views.data, name="main-admin"),
    path('assets/', include('assets.urls'), name= "assets"),
    path('status/', views.status, name="main-status")

]
