from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import Mentor


class Course(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=55)
    description = RichTextField()
    image = models.ImageField(upload_to='course/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
