from django.shortcuts import render
from django.views import generic
from .models import Course
from django.http import HttpResponseRedirect

# Create your views here.
class CourseView(generic.ListView):

    model = Course
    template_name='courses.html'

    def get_queryset(self):
        return Course.objects.all()



def myview(request):
    if request.user.is_authenticated==False:
        return HttpResponseRedirect("login/")
