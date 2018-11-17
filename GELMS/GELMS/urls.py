"""GELMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from courses.views import CourseView
from announcements.views import AnnouncementView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('courses/', TemplateView.as_view(template_name='courses.html'), name='courses'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('settings/', TemplateView.as_view(template_name='settings.html'), name='settings'),
    #path('announcements/', TemplateView.as_view(template_name='announcements.html'), name='announcements'),
    path('syllabus/', TemplateView.as_view(template_name='syllabus.html'), name='syllabus'),
    path('people/', TemplateView.as_view(template_name='people.html'), name='people'),
    path('tools/', TemplateView.as_view(template_name='tools.html'), name='tools'),
    path('', TemplateView.as_view(template_name='dashboard.html'), name='home'),
    path('courses/', CourseView.as_view(), name = 'courses'),
    path('announcements/', AnnouncementView.as_view(), name = 'announcements'),
]
