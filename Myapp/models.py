from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    full_name= models.CharField(max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    mobile =models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects =CustomUserManager()
    
    def __str__(self):
        return self.email



class Postfile(models.Model):
    tweet_post = models.CharField(max_length=100)
    upload=models.ImageField(upload_to='shivilafile')
    

class TwitterKey(models.Model):
    API_KEY=models.CharField(max_length=100)
    API_SECRET=models.CharField(max_length=100)
    ACCESS_TOKEN=models.CharField(max_length=100)
    ACCESS_TOKEN_SECRET=models.CharField(max_length=100)
    twitter_key=models.CharField(max_length=100,blank=True)

def __str__(self):
    return self.API_KEY