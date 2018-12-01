from django.shortcuts import get_object_or_404, redirect, render, reverse,HttpResponseRedirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from courses.models import Course
from .forms import ToolForm
from .models import Tool

# Create your views here.
class ToolsView(generic.View):

    @csrf_exempt
    def course_tools(request, course_name):

        course = get_object_or_404(Course, name=course_name)
        tool = get_object_or_404(Tool, course=course)

        if request.method == "POST":
            form = ToolForm(request.POST, instance = tool)
            if form.is_valid():
                tool = form.save(commit=False)
                tool.save()
        else:
            form = ToolForm(initial={'status':tool.status})

        form.fields['status'].widget.attrs = {'class':'form-control'}

        def user_is_registered(course=course):
            if course.teachers.filter(uid=request.user.custom_user.uid):
                return True
            if course.graders.filter(uid=request.user.custom_user.uid):
                return True
            if course.students.filter(uid=request.user.custom_user.uid):
                return True
            return False

        return render(request, 'tools.html', {'course': course, 'form':form, 'user_is_registered':user_is_registered})
