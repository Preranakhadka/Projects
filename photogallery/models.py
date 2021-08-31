from django.db import models
from django.contrib.auth import get_user_model
import datetime
import os 
def filepath(request,filename):
	old_filename=filename
	timenow="%s%s" % (timenow,old_filename)
	return os.path.join('/uploads',filename)


# Create your models here.
class Image(models.Model):
	title=models.CharField(max_length=255)
	photo=models.ImageField(upload_to = filepath,null=True,blank=True)
	user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	description=models.CharField(max_length=255)
	date=models.DateTimeField(auto_now_add=True)

