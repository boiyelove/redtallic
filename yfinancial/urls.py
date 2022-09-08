from django.conf.urls import url
from . import views



urlpatterns = {
	url(r"^get_tickers/$", views.get_tickers, name='get_tickers'),
	url(r"^refresh/$", views.get_tickers, name='get_tickers'),
	url(r"^subscriber/$", views.get_tickers, name='get_tickers'),
}