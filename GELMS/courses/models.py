from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your models here.
class Course(models.Model):
    cid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=7)
    title = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    students = models.ManyToManyField(CustomUser, related_name='course_students', limit_choices_to={'status': 'Student'}, blank=True)
    grader = models.ManyToManyField(CustomUser, related_name='course_grader', limit_choices_to={'status': 'Grader'}, blank=True)
    teacher = models.ManyToManyField(CustomUser, related_name='course_teacher', limit_choices_to={'status': 'Teacher'}, blank=True)

    def __str__(self):
        return self.name

    def people(self):
        return self.students.all() | self.grader.all() | self.teacher.all()
