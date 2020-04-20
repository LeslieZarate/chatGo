from django.contrib import admin
from.models import Chat

class ChatAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name','type_chat')
    

admin.site.register(Chat, ChatAdmin)
