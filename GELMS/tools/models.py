from django.db import models
from courses.models import Course

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    DOMAIN_CHOICES = (
        ('Art', 'Art'),
        ('Computer Science', 'Computer Science'),
        ('Engineering', 'Engineering'),
        ('History', 'History'),
        ('Literature', 'Literature'),
        ('Math', 'Math'),
        ('Music', 'Music'),
        ('Physics', 'Physics'),
        ('Political Science', 'Political Science'),
        )
    domain = models.CharField(max_length=30, choices=DOMAIN_CHOICES, default='Art')
    course = models.ForeignKey(Course, related_name='course_tools', blank=True, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
