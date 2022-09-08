from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def index(request):
	template = 'webcore/home.html'
	context = {}
	return render(request, template, context)

def newsletter_signup(request):
	news_signup = NewsletterForm(request.POST or None)
	if news_signup.is_valid():
		email = news_signup.clean_data.get('email')
		Newsletter(email = email)
		message.success(request, "You are now on our list, you're hear from us from time to time")
		return HttpResponseRedirect('/')

def contacted(request):
	new_contact = ContactForm(request.POST or None)
	if news_contact.is_valid():
		email = news_signup.clean_data.get('email')
		Newsletter(email = email)
		message.success(request, "You are now on our list, you're hear from us from time to time")
		return HttpResponseRedirect('/')

def handler400(request):
	template = '400.html'
	context = {}
	return render(request, template, context)

def handler403(request):
	template = '403.html'
	context = {}
	return render(request, template, context)

def handler404(request):
	template = '404.html'
	context = {}
	return render(request, template, context)

def handler500(request):
	template = '500.html'
	context = {}
	return render(request, template, context)
