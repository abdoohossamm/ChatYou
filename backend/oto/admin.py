from django.contrib import admin
from .models import Chat, Contact, Message
# Register your models here.
admin.site.register(Contact)
admin.site.register(Chat)
admin.site.register(Message)
