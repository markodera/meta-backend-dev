from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token

# Create your models here.

GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('rather_not_say', 'Rather not say')
]
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=225, unique=True, null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username} and {self.email}"
    
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null= True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER,blank=True, null=True)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if self.date_of_birth > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future")
    def __str__(self):
        return f"{self.user.username}'s profile"
    
