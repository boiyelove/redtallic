from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.contrib.auth.forms import User
from .models import User_Messages



class MessageForm(forms.Form):
	class Meta:
		model = User_Messages
		exclude = ['sent_on', 'read', ]


class SubscribeForm(forms.Form):
	email = forms.EmailField()


