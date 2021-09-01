from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.user and request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            context['error'] = str(form.errors)
    return render(request, 'sign_up.html', context)


def login_user(request):
    context = {}
    if request.user and request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['error'] = 'Username or password is incorrect!'
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


def logout_user(request):
    # if request.method == 'POST':
    #     logout(request)
    logout(request)
    return redirect('/accounts/login')
