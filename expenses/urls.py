from django.contrib import admin

from django.urls import path
from . import views


urlpatterns = [
    path('expenses/', views.expense, name="expense"),
    path('upload/', views.upload, name="upload"),
]