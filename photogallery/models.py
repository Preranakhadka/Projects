from django.db import models
from django.contrib.auth import get_user_model

def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.id, filename)

# Create your models here.
class Image(models.Model):
	title=models.CharField(max_length=255)
	photo=models.ImageField(upload_to = user_directory_path)
	user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	description=models.CharField(max_length=255)
	date=models.DateTimeField(auto_now_add=True)