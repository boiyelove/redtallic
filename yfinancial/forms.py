from django import forms

class CreditCardForm(forms.Form):
	payment_method_nonce = self.cleaned_data['payment_method_nonce']

	def clean(self):
		result = braintree.Transaction.sale({
			"amount": grand_total_amount,
			"payment_method_nonce" : payment_method_nonce,
			"options" : {
				"submit_for_settlement" : False
			}
		})
		if result.is_success:
			#dont change the customer yet - instead get the transaction
			# id and use that later to complete the sale.
			self.cleaned_data['braintree_transaction_id'] = result.transaction.id
		else:
			errors = ", ".join([e.message for e in result.errors.deep_errors])
			raise form.ValidationError(errors)