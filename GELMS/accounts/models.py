from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, related_name='custom_user', on_delete=models.CASCADE)
    uid = models.CharField(max_length=100, unique=True)
    STATUS_CHOICES = (
        ('Student', 'Student'),
        ('Grader', 'Grader'),
        ('Teacher', 'Teacher'),
        )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ST')

    def __str__(self):
        return "UID: " + self.uid + " | Name: " + self.user.first_name + " " + self.user.last_name

    def user_courses(self):
        if self.status == 'Teacher':
            return self.course_teacher.all()
        elif self.status == 'Grader':
            return self.course_grader.all()
        else:
            return self.course_students.all()
