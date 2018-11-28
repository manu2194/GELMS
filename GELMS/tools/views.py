from django.shortcuts import render, get_object_or_404
from django.views import generic
from courses.models import Course

# Create your views here.
class ToolsView(generic.View):

    def course_tools(request, course_name):
        course = get_object_or_404(Course, name=course_name)

        def user_is_registered(course=course):
            if course.teachers.filter(uid=request.user.custom_user.uid):
                return True
            if course.graders.filter(uid=request.user.custom_user.uid):
                return True
            if course.students.filter(uid=request.user.custom_user.uid):
                return True
            return False

        return render(request, 'tools.html', {'course': course, 'user_is_registered':user_is_registered})
