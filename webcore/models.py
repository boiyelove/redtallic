from django.db import models

# Create your models here.
class Newsletter(models.Model):
	email = models.EmailField()
	created = models.DateTimeField(auto_now = True, auto_now_add=False)
	updated = models.DateTimeField(auto_now = False, auto_now_add=True)


class Banner(models.Model):
	title = models.CharField(max_length = 30)
	desc = models.CharField(max_length = 60)
	btn_link = models.URLField()
	btn_title = models.CharField(max_length = 18)
	created = models.DateTimeField(auto_now = True, auto_now_add=False)
	updated = models.DateTimeField(auto_now = False, auto_now_add=True)

class Contact(models.Model):
	email =models.EmailField()
	subject = models.CharField(max_length = 30)
	content = models.TextField()
	created = models.DateTimeField(auto_now = True, auto_now_add=False)
	updated = models.DateTimeField(auto_now = False, auto_now_add=True)