from django.db import models
from courses.models import Course

# Create your models here.
class Announcement(models.Model):
    aid = models.CharField(max_length=20)
    content = models.TextField()
