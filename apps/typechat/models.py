from django.db import models

class TypeChat(models.Model):
    name = models.CharField(max_length=100,verbose_name='nombre',)
    def __str__(self):
        return self.name
