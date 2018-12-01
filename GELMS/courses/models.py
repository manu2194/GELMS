from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=7, unique=True, help_text='e.g. ENPM613')
    title = models.CharField(max_length=200, help_text='e.g. Software Design and Implementation')
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
    students = models.ManyToManyField(CustomUser, related_name='course_students', limit_choices_to={'status': 'Student'}, blank=True)
    graders = models.ManyToManyField(CustomUser, related_name='course_graders', limit_choices_to={'status': 'Grader'}, blank=True)
    teachers = models.ManyToManyField(CustomUser, related_name='course_teachers', limit_choices_to={'status': 'Teacher'}, blank=True)

    def __str__(self):
        return self.name

    def get_students(self):
        return self.students.order_by('user__last_name')

    def get_graders(self):
        return self.graders.order_by('user__last_name')

    def get_teachers(self):
        return self.teachers.order_by('user__last_name')

    def people(self):
        return self.students.all() | self.grader.all() | self.teacher.all()

    def get_syllabus(self):
        return self.course_syllabus.order_by('due_date')

    def get_announcements(self):
        return self.course_announcements.order_by('-publish_date')

    def get_tools(self):
        return self.course_tools
