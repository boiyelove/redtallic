import braintree
from django.shortcuts import render
from django.conf import settings


# Create your views here.


braintree.Configuration.configure(braintree.Environment.Sandbox,
	merchant_id = settings.BRAINTREE_MERCHANT_ID,
	public_key = settings.BRAINTREE_PUBLIC_KEY,
	private_key = settings.BRAINTREE_PRIVATE_KEY)


def payment_view(request):
	if request.method == "GET":
		request.session['braintree_client_token'] = braintree.CLientToken.generate()

		context = {}
		template = ''
		return render(request, template, context)
	else:
		if not form.is_valid():
			return render(request, template, context)
		else:
			pass

def get_tickers(request):
	pass