from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class Userprofile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, unique = True)
	home_phone = models.CharField(max_length = 12, null = True, blank = True)
	office_phone = models.CharField(max_length = 12, null = True, blank = True)
	address = models.CharField(max_length = 60, null = True, blank = True)
	mobile = models.CharField(max_length = 12, null = True, blank = True)
	about = models.TextField(null=True)



class EmailConfirmed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)

	def __str__(self):
		return self.confirmed

	def activate_user_email(self):
		activation_url = "%s%s" %(settings.SITE_URL, reverse("activation_view", args[self.activation_key]))
		context = {
			"activation_key": self.activation_key,
			"activation_url": activation_url,
			"user": self.user.first_name,
		}
		message = render_to_string("accounts/activation_message.txt", context)
		subject = "Activate your email"
		self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.user.email], kwargs)


class EmailMarketingSignUp(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email


