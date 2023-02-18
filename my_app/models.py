from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    full_name = models.CharField(max_length = 35, blank= True)
    phone_number = models.CharField(max_length=11, blank=True)
    