from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#Class for signup and login
class CustomUser(AbstractUser):
    email = models.EmailField(
        blank=False, null= False, unique=True, verbose_name="Email Address"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# test data for modelform practice
class Test(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name