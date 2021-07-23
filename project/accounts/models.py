from django.contrib.auth.models import User
from django.db import models


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='mentor/')
    organization = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    youtube_link = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False, blank=True)

