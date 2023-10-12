from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='default.jpg')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
class NewsletterUser(models.Model):

    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email