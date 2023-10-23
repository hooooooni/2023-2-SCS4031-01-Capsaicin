from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """        
    def create_user(self, phone_number, fullname, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not phone_number:
            raise ValueError(_('The phone_number must be set'))
        if not fullname:
            raise ValueError(_('The fullname must be set'))
        user = self.model(phone_number=phone_number, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)
    


class User(AbstractUser):
    fullname = models.CharField(_('fullname'), max_length=4)
    phone_number = models.CharField(_('phone number'), unique=True, max_length=11)
    password = models.CharField('password', max_length=128)
    username = models.CharField(max_length=1, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password', 'fullname']

    objects = CustomUserManager()


    def __str__(self):
        return self.phone_number