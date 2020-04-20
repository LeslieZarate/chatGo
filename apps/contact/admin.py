from django.contrib import admin
from.models import Contact

class ContactAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','user')
   


admin.site.register(Contact, ContactAdmin)
