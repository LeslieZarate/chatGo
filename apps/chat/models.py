from django.db import models
from typechat.models import TypeChat
from contact.models import Contact

class Chat(models.Model):
    name = models.CharField(verbose_name='Nombre',max_length=50)
    avatar = models.ImageField(verbose_name='avatar', null=True, blank=True)
    date_registration =  models.DateTimeField(auto_now_add=True , verbose_name=u'Fecha de Registro')
    type_chat = models.ForeignKey( TypeChat , on_delete=models.SET_NULL, null=True, verbose_name='Tipo Chat' )
    participants = models.ManyToManyField(Contact, related_name='chat', blank=True , verbose_name='Participantes')
   
    def __str__(self):
        return self.name
