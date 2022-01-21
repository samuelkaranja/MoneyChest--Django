from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('deposit/', views.Deposit, name="deposit"),
    path('PlayChests/', views.PlayChests, name="PlayChests"),
]