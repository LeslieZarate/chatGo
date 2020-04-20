from django.contrib import admin
from django.urls import path
from  admin import admin_site
from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    #url('myadmin/', admin_site.urls),
    url('user/', include('user.urls', namespace='users')),
    url('contact/', include('contact.urls', namespace='contacts')),
    url('message/', include('message.urls', namespace='message')),
    url('',include('chat.urls', namespace='home')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
