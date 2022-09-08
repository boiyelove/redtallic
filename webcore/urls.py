from django.conf.urls import url, handler400, handler403, handler404, handler500
from . import views


handler400 = views.handler400
handler403 = views.handler403
handler404 = views.handler404
handler500 = views.handler500
urlpatterns = [
	url(r'$',views.index, name = 'home'),
	url(r'about/$',views.index, name = 'about'),
	url(r'contact/$',views.index, name = 'contact'),
	url(r'contacted/$',views.contacted, name = 'contact'),


]
