from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    people = models.ManyToManyField(User, related_name='people', blank=True)

    def __str__(self):
        return self.name
