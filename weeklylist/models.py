from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
	tagline = models.CharField(max_length=255)
	friend = models.ForeignKey(User, related_name='lists')
	subject = models.CharField(max_length=255)
	signoff = models.TextField(max_length=4000)
	created_at = models.DateTimeField(auto_now_add=True)
	image = models.FileField(null=True, blank=True)