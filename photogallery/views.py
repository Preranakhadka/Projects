from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image


@login_required
def home(request):
	context = {}
	images = request.user.image_set.all()
	context['images'] = images
	return render(request, 'image_index.html', context)


@login_required
def upload(request):
	if request.method == 'POST':
		title = request.POST['title']
		description = request.POST['description']
		user = request.user
		photo = request.FILES['photo']
		Image(title=title, description=description, user=user, photo=photo).save()
	return redirect('/')