from django.db import models
from courses.models import Course

# Create your models here.
class Announcement(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='course_announcements', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "content = {}, course = {}".format(self.content,self.course)
