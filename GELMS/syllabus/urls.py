from django.contrib import admin
from django.urls import path
from . import views

name = 'syllabus'
urlpatterns = [
    path('syllabus_delete/',views.SyllabusView.syllabus_delete,name="syllabus_delete"),
]