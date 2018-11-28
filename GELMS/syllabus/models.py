from django.db import models
from courses.models import Course
import datetime



# Create your models here.
class Syllabus(models.Model):
    content = models.CharField(max_length=500)
    course = models.ForeignKey(Course, related_name='course_syllabus', blank=True, on_delete=models.CASCADE)
    due_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return "content = {}, course = {}, publish date = {}".format(self.content,self.course,self.due_date)
