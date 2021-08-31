from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image


@login_required
def home(request):
     if request.method=="POST":
     	img=Item()
     	img.title=request.POST.get('title')
     	img.description=request.POST.get('description')

     	if len(request.FILES)!=0:
     		img.photo=request.FILES['photo']
     	img.save()
     	return redirect(request, 'index.html')
