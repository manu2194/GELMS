from django.shortcuts import render
from django.views import generic
from .models import Course
from django.http import HttpResponseRedirect


# Create your views here.
class CourseView(generic.ListView):

    def user_courses(request):
        return render(request, 'courses.html')


    def get_queryset(self):
        return Course.objects.all()
