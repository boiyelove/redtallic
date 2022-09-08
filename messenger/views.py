from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import User_Notifications, User_Messages, Subscribe_list
from .forms import MessageForm, SubscribeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


@login_required
def messager(request):

	me = request.user
	rece = request.POST.get('receipient')
	try:
		rece = User.objects.get(username = rece)
	except DoesNotExist:
		return HttpResponse('Sorry Invalid User')

	new_message = request.POST.get('content')
	print('user_id is:', rece)
	print('user_id is:', new_message)

	if rece and new_message :
		sender = me
		data = {'sender': me,
		'content' : new_message,
		'receipient' : rece,}
		a = MessageForm(data)
		if a.is_valid():
			print('message is valid \n')
			content = a.cleaned_data.get('content')
			receipient = a.cleaned_data.get('receipient')
			new_messa = User_Messages.objects.create(sender = request.user,
				receipient = rece,
				content = new_message)
			new_messa.save()
			print('message is sent \n')
			return  HttpResponse('Your Message Was Sent Successfully. <a href="/account/">Go to account</a>')
	return  HttpResponse('Something went wrong,or you didnt type in any content <a href="/">Go Home</a>')

def new_message(request):
	me = request.user
	user_id = request.POST.get('email')
	print('user_id is:', user_id)
	print('me is:', me)
	try:
		user_id = User.objects.get(email = user_id)
	except:
		user_id = None
	receipient = user_id
	context = {'title': 'New Message', 'form': MessageForm, 'receipient': receipient}
	template = 'new_message.html'
	return render (request, template, context)


def subscribe(request):
	email = SubscribeForm(request.POST or None)
	context = {}
	if email.is_valid():
		email = email.cleaned_data.get('email')
		new_subcriber, created = Subscribe_list.objects.get_or_create(email = email)
		if created:
			context = {'msg' : 'You have successfully subscribed, you wil be notified'}
		else:
			context = {'msg' : 'You have already subscribed, you wil be notified'}
		template = 'thanks.html'
		return render(request, template, context)
	context = {'msg' : 'You have made an invalid entry'}
	template = 'thanks.html'
	return render(request, template, context)

@login_required
def inboxview(request):
	me = request.user
	all_received = User_Messages.objects.all().filter(receipient = me)
	context = {'info_list' : all_received,
	'title' :'Inbox'}
	template = 'inbox_list.html'
	return render(request, template, context)

@login_required
def outboxview(request):
	me = request.user
	all_received = User_Messages.objects.all().filter(sender = me)	
	context = {'info_list' : all_received,
	'title' : 'Outbox'}
	template = 'outbox_list.html'
	return render(request, template, context)


def conversview(request, pk):
	from itertools import chain
	me = request.user
	rece = User.objects.get(id = pk)
	sent = User_messages.objects.get(sender = me, receiver = rece )
	received =User_messages.objects.get(sender = rece, receiver = me)
	allmessages = User_Messages.objects.order_by('sender', 'receiver', -'sent_on').distinct('sender', 'receiver')
	meanduser = sorted(
		(chain(sent, received)),
			key=lambda instance: instance.sent_on)
	context ={'message_ist': meanduser}
	template_name = 'inbox_list.html'
	return render(request, template, context)


def single_message(request, pk):
	try:
		message = User_Messages.objects.get(pk = pk)
		if request.user == message.receipient:
			message.read = True
			message.save()
			msg_btn = 'Reply'
			sender_or = 'Sent From:'
		else:
			msg_btn = 'Message'
			sender_or = 'Sent To:'
	except ObjectDoesNotExist:
		return HttpResponse('Sorry the requested message does not exist')
	title = 'Message'
	context = {'title': 'Message', 'message':  message, 'msg_btn': msg_btn, 'sender_or' : sender_or}
	template = 'single_message.html'
	return render (request, template, context)
