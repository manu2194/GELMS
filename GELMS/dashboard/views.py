from django.shortcuts import render, get_object_or_404
from django.views import generic
from courses.models import Course

# Create your views here.
class DashboardView(generic.View):

        def user_dashboard(request):
            return render(request, 'dashboard.html', {})

        def help(request):
            return render(request, 'help.html')
