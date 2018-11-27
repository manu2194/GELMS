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
from announcements.views import AnnouncementView
from courses.views import CourseView
from dashboard.views import DashboardView
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from people.views import PeopleView
from settings.views import SettingsView
from syllabus.views import SyllabusView
from tools.views import ToolsView

urlpatterns = [
    path('', DashboardView.user_dashboard, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('courses/', CourseView.user_courses, name = 'courses'),
    path('dashboard/', DashboardView.user_dashboard, name = 'dashboard'),
    path('settings/', SettingsView.user_settings, name='settings'),
    path('<course_name>/announcements', AnnouncementView.course_announcements, name = 'announcements'),
    path('<course_name>/syllabus/<syllabus_id>/syllabus_delete',SyllabusView.syllabus_delete,name="syllabus_delete"),
    path('<course_name>/syllabus/<syllabus_id>/syllabus_edit',SyllabusView.syllabus_edit,name="syllabus_edit"),
    path('<course_name>/syllabus/', SyllabusView.course_syllabus, name='syllabus'),
    path('<course_name>/people/', PeopleView.course_people, name='people'),
    path('<course_name>/tools/', ToolsView.course_tools, name='tools'),
]
