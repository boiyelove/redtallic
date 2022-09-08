from django.conf.urls import url
from .views import UserProfileEditView
from . import views
#import views


urlpatterns = [
	#if the url contains string between the r^ and $ only, cll the relatd view
	url(r'^account/$', views.myDashboard, name = 'dashboard'),
	url(r'^account/change_password/$', views.changepassword, name = 'changepassword'),
	url(r'^login/$',views.myLogin, name = 'login'),
	url(r'^logout/$', views.myLogout, name = 'logout'),
	url(r'^register/$', views.myRegister, name = 'register'),
	url(r'^profile/$', views.UserProfileEditView.as_view(), name = 'profile_edit'),
	url(r'^profile/(?P<pk>[0-9]+)/$', views.UserProfileDetailView.as_view(), name='user_profile_detail'),
    url(r'^account/activate/(?P<activation_key>\w+)/$', views.activation_view, name='activation_view'),


]


