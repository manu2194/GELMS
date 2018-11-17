from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class CustomUser(models.Model):
    user = models.OneToOneField(User, related_name='custom_user', on_delete=models.CASCADE)
    uid = models.CharField(max_length=100)
    STATUS_CHOICES = (
        ('Student', 'Student'),
        ('Grader', 'Grader'),
        ('Teacher', 'Teacher'),
        )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ST')

    def __str__(self):
        return self.uid
