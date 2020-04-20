from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class MyUserManager(BaseUserManager,):
    def create_user(self, email, password=None,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model( email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password,**extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
		)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name="Correo electrónico", unique=True)
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento",blank=True,null=True)
    avatar = models.ImageField(verbose_name='avatar', null=True, blank=True)
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email
