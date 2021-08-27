from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import user_passes_test


urlpatterns = [
    path('', views.login_user, name="login"),
    path('sign_up/', views.sign_up, name="sign-up"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
