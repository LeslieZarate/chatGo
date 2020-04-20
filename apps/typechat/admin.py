from django.contrib import admin
from .models import TypeChat

class TypeChat_Admin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name')
   
admin.site.register(TypeChat, TypeChat_Admin)