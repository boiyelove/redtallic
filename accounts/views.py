import re
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Userprofile
from .forms import LoginForm, RegisterForm, ProfileForm, PasswordChangeForm, PasswordForm

# Create your views here.
@login_required
def myDashboard(request):

	context = {}
	template = 'account/dashboard.html'
	return render (request, template, context)


def myLogin(request):
	if not request.user.is_anonymous() and request.user.is_authenticated():
		return HttpResponseRedirect('/account/')
	nex = (request.POST.get('next') or None)
	loginform = LoginForm(request.POST or None)
	if loginform.is_valid():
		uname = loginform.cleaned_data.get('email')
		password = loginform.cleaned_data.get('password')
		user = authenticate(username=uname, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if nex is None:
					messages.success(request, "Successfully Logged In. Welcome Back!")
					return HttpResponseRedirect('/account/')
				else:
					return HttpResponseRedirect(request.POST.get('next'))
	context = {'loginform' : loginform}
	
	template = 'accounts/login.html'
	return render(request, template, context)

def myLogout(request):
	logout(request)
	messages.success(request, "<strong>Successfully Logged out</strong>. Feel free to <a href='%s'>login</a> again." %(reverse("auth_login")), extra_tags='safe, abc')
	messages.warning(request, "There's a warning.")
	messages.error(request, "There's an error.")
	return HttpResponseRedirect('/')

def myRegister(request):
	if not request.user.is_anonymous() and request.user.is_authenticated():
		return HttpResponseRedirect('/account/')	
	registerform = RegisterForm(request.POST or None)
	if registerform.is_valid():
		email = registerform.cleaned_data.get('email')
		first_name = registerform.cleaned_data.get('first_name')
		new_user = User.objects.create_user(first_name = first_name,
			email = email,
			lastname= lastname)

		new_user_login = Userprofile.objects.get(user = new_user)
		return HttpResponseRedirect ('/login/')
	title = "New Account Registration"
	context = {'title':title, 'registerform': registerform}
	template = 'accounts/register.html'
	return render(request, template, context)

class UserProfileDetailView(DetailView):
	model = get_user_model()
	pk = 'id'
	template_name = 'user_detail.html'
	
	def get_object(self, queryset=None):
		user = super(UserProfileDetailView, self).get_object(queryset)
		Userprofile.objects.get_or_create(user = user)
		return user

class UserProfileEditView(UpdateView):
	model = Userprofile
	form_class = ProfileForm
	template_name = 'profile.html'

	def get_object(self, quesryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse("profile", kwargs={'id': self.request.user.id})

@login_required
def changepassword(request):
	passwordform = PasswordChangeForm(request.POST or None)
	if passwordform.is_valid():
		print('')
		print('')
		print('')
		print('password form is valid')
		password = passwordform.cleaned_data.get('password')
		me = request.user
		me.set_password(password)
		me.save()
		msg =  "You have successfully changed your password. Please Login with your new password"
		context = {'msg' : msg}
		template = 'thanks.html'
		return render(request, template, context)
	title = "Change Your Password"
	context = {'title':title, 'form': passwordform}	
	template = 'passwordform.html'
	return render(request, template, context)

SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
	if SHA1_RE.search(activation_key):
		try:
			instance = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			instance = None
			message.success(request, "There was an error")
			return HttpResponseRedirect("/")
		if instance is not None and not instance.confirmed:
			passdata = PasswordForm(request.POST or None)
			if passdata.is_valid():
				passdata = passdata.cleaned_data.get('password1')
				user = instance.user
				force_login(user)
				user.set_password(passdata)
				user.is_active=True
				user.save()
				instance.confirmed = True
				instance.activations_key = "confirmed"
				instance.save()
				messages.success(request,"Your password was set successfully, please login")
				return HttpResponseRedirect('login')
			messages.info(request, "Please choose a password for your account to complete activation")
			template = 'accounts/passwords.html'
			context = {'passwordform': passdata}
			return render(request, template, context)

		elif instance is not None and instance.Confirmed == "Confirmed":
			message.success(request, "You have already confirmed your email, please login")
			HttpResponseRedirect('/login/')
		else:
			page_message = ""
		context = {"page_message" : page_message}
		template = "accounts/activation_complete.html"
		return render(request, template, context)
	else:
		raise Http404

