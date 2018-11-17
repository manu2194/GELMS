from django.shortcuts import render
from django.views import generic
from .models import Announcement
# Create your views here.
class AnnouncementView(generic.ListView):

    model = Announcement
    template_name='announcements.html'

    def get_queryset(self):
        return Announcement.objects.all()
