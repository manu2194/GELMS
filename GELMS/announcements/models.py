from django.db import models
from courses.models import Course

# Create your models here.
class Announcement(models.Model):
    content = models.CharField(max_length=1000)
    course = models.ForeignKey(Course, related_name='course_announcements', blank=True, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(blank=True,null=True)
    publisher = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "content = {}, course = {}".format(self.content,self.course)
