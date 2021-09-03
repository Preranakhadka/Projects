from django.contrib import admin

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('new_expenses', views.new_expenses, name="new_expenses"),
]