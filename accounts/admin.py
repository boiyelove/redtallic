from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib import admin
# Register your models here.
from .models import EmailConfirmed, EmailMarketingSignUp

admin.site.register(EmailConfirmed)


class EmailMarketingSignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'timestamp']
	class Meta:
		model = EmailMarketingSignUp


admin.site.register(EmailMarketingSignUp, EmailMarketingSignUpAdmin)