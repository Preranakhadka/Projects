from django.contrib import admin

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.new_expenses, name="expenses"),
    path('edit/', views.edit_expenses, name="edit-expenses"),
    path('delete/', views.delete_expenses, name="delete-expenses"),

]
