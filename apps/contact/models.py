from django.db import models
from user.models import User

class Contact(models.Model):
    user = models.ForeignKey( User, related_name='contact',on_delete=models.SET_NULL, null=True, verbose_name='usuario')
    friends = models.ManyToManyField('self', blank=True,verbose_name='amigos')

    def __str__(self):
        return self.user.email
