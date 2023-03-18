from email.policy import default
from unittest.util import _MAX_LENGTH
import django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def get_profile_location(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'



# Create your models here.
class Account(AbstractBaseUser):

    email           = models.EmailField(verbose_name = 'email', max_length= 150, unique= True)
    username        = models.CharField(max_length= 150, unique= True)

    creation_date   = models.DateTimeField(auto_now_add= True)

    is_admin        = models.BooleanField(default= False)
    is_active       = models.BooleanField(default= True)
    is_staff        = models.BooleanField(default= False)
    is_superuser    = models.BooleanField(default= False)
    profile_image   = models.ImageField(max_length = 255, upload_to = get_profile_location, null = True, blank = True)
    hide_email      = models.BooleanField(default= True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    
    
