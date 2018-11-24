from django.shortcuts import render, get_object_or_404
from django.views import generic
from courses.models import Course

# Create your views here.
class SyllabusView(generic.View):

    def course_syllabus(request, course_name):
        course = get_object_or_404(Course, name=course_name)
        return render(request, 'syllabus.html', {'course': course})
