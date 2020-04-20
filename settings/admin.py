from django.contrib.admin import AdminSite
from user.models import User
from user.admin import CustomUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

class MyAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"

admin_site = MyAdminSite(name='myadmin')
admin_site.register(User,CustomUserAdmin)
admin_site.register(Group, GroupAdmin)