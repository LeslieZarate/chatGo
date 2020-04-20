from django.contrib import admin
from message.models import Message

class MessageAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','contact', 'chat','content')
admin.site.register(Message, MessageAdmin)