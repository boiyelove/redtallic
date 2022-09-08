from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from .models import Userprofile



User = get_user_model()

class SearchForm(forms.Form):
	stock_item = forms.CharField(max_length ='3')




class LoginForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError("Invalid Password")
		elif user is None:
			pass
		else:
			return password

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Userprofile
		exclude = ['user', 'first_login', ]


class RegisterForm(forms.Form):
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	email = forms.EmailField()
	email1 = forms.EmailField()

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email1 = self.cleaned_data.get('email1')
		try:
			user = User.objects.get(email = email)
			if user:
				raise forms.ValidationError('This email has already been registered. Please check and try again or reset your password.')
		except ObjectDoesNotExist:
			if email and email1 and email != email1:
				raise forms.ValidationError('The email addresses provided do not match')
			return email
	
class PasswordChangeForm(forms.Form):
	password1 = forms.CharField(label='Password', \
					widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password Confirmation', \
					widget=forms.PasswordInput())

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match")
		return password2



class RegrForm(forms.ModelForm):
	email = forms.EmailField(label='Your Email')
	firstname= forms.CharField(label='First Name')
	lastname = forms.CharField(label='Last Name')

	class Meta:
		model = User
		fields = ['username', 'email', 'firstname', 'lastname']


	def clean_email(self):
		email = self.cleaned_data.get("email")
		user_count = User.objects.filter(email=email).count()
		if user_count > 0:
			raise forms.ValidationError("This email has already been registered. Please check and try again or reset your password.")
		return email



class PasswordForm(forms.Form):
	password1 = forms.CharField(label='Password', \
					widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password Confirmation', \
					widget=forms.PasswordInput())


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match")
		return password2