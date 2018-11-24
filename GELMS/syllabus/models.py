from django.db import models
from courses.models import Course

# Create your models here.
class Syllabus(models.Model):
    content = models.TextField()
    publish_date = models.DateField()
    
