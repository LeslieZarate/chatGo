from django.db import models
from contact.models import Contact
from chat.models import Chat

class Message(models.Model):    
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    content = models.TextField(verbose_name='Contenido', null=True, blank=True)
    img = models.ImageField(verbose_name='avatar', null=True, blank=True)
    contact = models.ForeignKey( Contact, related_name='message', on_delete=models.SET_NULL, null=True ,verbose_name='Contacto')    
    chat = models.ForeignKey( Chat, related_name='message',on_delete=models.SET_NULL, null=True ,verbose_name='Chat') 

    def __str__(self):
        return self.content
