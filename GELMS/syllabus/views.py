import datetime
from datetime import datetime, timezone

from django.shortcuts import get_object_or_404, redirect, render, reverse,HttpResponseRedirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from courses.models import Course

from .forms import SyllabusForm
from .models import Syllabus

# Create your views here.

class SyllabusView(generic.View):
    
    @csrf_exempt
    def course_syllabus(request, course_name):
        
        if request.method == "POST":
            course_ob = get_object_or_404(Course, name=course_name)
            #syllabus_edit = get_object_or_404(Syllabus, course=course_ob)
            try:
                form = SyllabusForm(request.POST)
                #print(form)
                if form.is_valid():
                    
                    syllabus = form.save(commit=False)
                    syllabus.course = course_ob
                    syllabus.publish_date = datetime.now()
                    syllabus.save()
            except:
                form = SyllabusForm(request.POST, instance = syllabus_edit)
                if form.is_valid():
                    syllabus_edit = form.save(commit=False)
                    syllabus_edit.publish_date = datetime.now()
                    syllabus_edit.save()

        else:
            form = SyllabusForm()

        form.fields['content'].widget.attrs = {'class':'form-control'}
        course = get_object_or_404(Course, name=course_name)
        # syllabus = get_object_or_404(Syllabus,course_id=course.id)
        # print(syllabus.content)
        return render(request, 'syllabus.html', {'course': course,'form':form})

    
    def get_queryset(self):
        return Syllabus.objects.all()

    def syllabus_delete(request,course_name,syllabus_id):
        course = get_object_or_404(Course, name=course_name) 
        syllabus = get_object_or_404(Syllabus,course= course,id=syllabus_id).delete()
        return redirect("syllabus",course_name)

    @csrf_exempt
    def syllabus_edit(request,course_name,syllabus_id):

        if request.method == "GET":
            course = get_object_or_404(Course, name=course_name)
            return render(request, 'syllabus_edit.html',{'course':course})

        elif request.method == "POST":
            course = get_object_or_404(Course, name=course_name)
            if request.POST.get("syllabus_edit_cancel"):
                return redirect("syllabus",course_name)