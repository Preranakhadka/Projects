from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
	return render( request,"index.html",context={})

def login_view(request):
	return render( request,"login.html",context={})