from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    displayName = models.CharField(max_length=255)
    photoUrl = models.ImageField(upload_to='images/user_photoURLs/')

class Address(models.Model):
    fullName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

