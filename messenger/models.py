from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.

def get_sentinel_user():
	return get_user_model().objects.get_or_create(username = 'deleted User')[0]

class User_Messages(models.Model):
	sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET(get_sentinel_user), related_name='writer')
	content = models.TextField(null = True, blank = True)
	receipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET(get_sentinel_user), related_name='reader')
	sent_on = models.DateTimeField(auto_now_add = True)
	read = models.BooleanField(default = False)

	def __str__(self):
		return content

class User_Notifications(models.Model):
	content = models.CharField(max_length=80)
	created_on = models.DateTimeField(auto_now = True, null = True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	def __str__(self):
		return content

class Subscribe_list(models.Model):
	email = models.EmailField()
	ABP = models.BooleanField(default = False, verbose_name = 'ab_positive')
	AB = models.BooleanField(default = False, verbose_name = 'ab_negative')
	BP = models.BooleanField(default = False, verbose_name = 'b_positive')
	BN = models.BooleanField(default = False, verbose_name = 'b_negative')
	AP = models.BooleanField(default = False, verbose_name= 'a_positive')
	AN = models.BooleanField(default = False, verbose_name = 'a_negative')
	OP = models.BooleanField(default = False, verbose_name = 'o_positive')
	ON = models.BooleanField(default = False, verbose_name = 'o_negative')
	general = models.BooleanField(default = True)
	created_on = models.DateTimeField(auto_now = True)

class contactus(models.Model):
	email = models.EmailField()
	