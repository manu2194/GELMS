from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Announcement
from courses.models import Course

# Create your views here.
class AnnouncementView(generic.View):

    def course_announcements(request, course_name):
        course = get_object_or_404(Course, name=course_name)
        return render(request, 'announcements.html', {'course': course})


    def get_queryset(self):
        return Announcement.objects.all()
