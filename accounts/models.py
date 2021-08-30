from django.db import models

# Create your models here.
class Image(models.Model):
	id=models.CharField(max_length=3,primary_key=True)
	title=models.CharField(max_length=255)
	photo=models.ImageField(upload_to="images")
	description=models.CharField(max_length=255)
	date=models.DateTimeField(auto_now_add=True)