from django.contrib import admin
from .models import User_Messages, User_Notifications, Subscribe_list

# Register your models here.

class User_MessagesAdmin(admin.ModelAdmin):
	pass


class User_NotificationsAdmin(admin.ModelAdmin):
	pass

class Subscribe_listAdmin(admin.ModelAdmin):
	list_display = ('email', 'ABP', 'AB', 'BP', 'BN', 'AP', 'AN', 'OP', 'ON', 'general') 

admin.site.register(Subscribe_list, Subscribe_listAdmin )
admin.site.register(User_Notifications)
admin.site.register(User_Messages)