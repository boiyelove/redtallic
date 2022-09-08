from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^subscribe/$', views.subscribe, name ='subscribe' ),
	url(r'^message/$', views.messager, name='messager'),
	url(r'^new_message/$', views.new_message, name='new_message'),
	url(r'^inbox/$', views.inboxview, name='myMessages'),
	url(r'^outbox/$', views.outboxview, name='mySentMessages'),
	url(r'^message/(?P<pk>[0-9]+)/$', views.single_message, name='single_message'),

]