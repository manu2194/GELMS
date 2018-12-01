from django.db import models
from courses.models import Course

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    #domain = models.CharField(max_length=30)
    course = models.OneToOneField(Course, related_name='course_tools', blank=True, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
