from django.shortcuts import render, get_object_or_404
from django.views import generic
from courses.models import Course

# Create your views here.
class SettingsView(generic.View):

        def user_settings(request):
            return render(request, 'settings.html', {})
