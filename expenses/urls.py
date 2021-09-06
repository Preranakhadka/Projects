from django.contrib import admin

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('expenses/', views.new_expenses, name="expenses"),
    path('expenses/', views.edit_expenses, name="expenses"),


]
