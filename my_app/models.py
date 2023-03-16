
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
vendor_list = (('Jumia','Jumia'), ('Konga', 'Konga'), ('Unknown', 'Unknown'))

class Customuser(AbstractUser):
    full_name = models.CharField(max_length = 35, blank= True)
    phone_number = models.CharField(max_length=11, blank=True)
    
class SavedProduct(models.Model):
    name = models.CharField(max_length=300, blank=False)
    price = models.CharField(max_length=20, blank=False)
    image_url = models.CharField(max_length=200, blank=False)
    product_url = models.CharField(max_length=100)
    product_id = models.CharField(max_length=30)
    owner = models.ForeignKey(Customuser, on_delete=models.CASCADE, null=True)
    vendor = models.CharField(choices=vendor_list, max_length=50, default='Unknown')
    date_added = models.DateTimeField(default=timezone.now)

