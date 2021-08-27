from django.shortcuts import render


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request,'accounts/index.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'accounts/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            login(request,user)
            return render(request,'accounts/index.html')
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return render(request,'accounts/logged_out.html')

