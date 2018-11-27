import datetime
from datetime import datetime, timezone

from django.shortcuts import get_object_or_404, redirect, render, reverse,HttpResponseRedirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from courses.models import Course

from .forms import AnnouncementForm
from .models import Announcement

# Create your views here.

class AnnouncementView(generic.View):
    
    @csrf_exempt
    def course_announcements(request, course_name):
        
        if request.method == "POST":
            course_ob = get_object_or_404(Course, name=course_name)
            #syllabus_edit = get_object_or_404(Syllabus, course=course_ob)
            try:
                form = AnnouncementForm(request.POST)
                #print(form)
                if form.is_valid():
                    
                    announcement = form.save(commit=False)
                    announcement.course = course_ob
                    announcement.publish_date = datetime.now()
                    announcement.save()
                    form = AnnouncementForm()
            except:
                form = AnnouncementForm(request.POST, instance = announcement_edit)
                if form.is_valid():
                    announcement_edit = form.save(commit=False)
                    announcement_edit.publish_date = datetime.now()
                    announcement_edit.save()

        else:
            form = AnnouncementForm()

        form.fields['content'].widget.attrs = {'class':'form-control'}
        course = get_object_or_404(Course, name=course_name)
        # syllabus = get_object_or_404(Syllabus,course_id=course.id)
        # print(syllabus.content)
        return render(request, 'announcements_temp.html', {'course': course,'form':form})

    
    def get_queryset(self):
        return Announcement.objects.all()

    def announcement_delete(request,course_name,announcement_id):
        course = get_object_or_404(Course, name=course_name) 
        announcement = get_object_or_404(Announcement,course= course,id=announcement_id).delete()
        return redirect("announcements",course_name)

    @csrf_exempt
    def announcement_edit(request,course_name,announcement_id):
        if request.method == "POST":
            course = get_object_or_404(Course, name=course_name)
            announcement_edit = get_object_or_404(Announcement, id = announcement_id)
            form = AnnouncementForm(request.POST, instance = announcement_edit)
            if form.is_valid():
                announcement_edit = form.save(commit=False)
                announcement_edit.publish_date = datetime.now()
                announcement_edit.save()
                return redirect("announcements",course_name)
        else:
            form = AnnouncementForm()

        form.fields['content'].widget.attrs = {'class':'form-control'}
        course = get_object_or_404(Course, name=course_name)
        announcement = get_object_or_404(Announcement, id = announcement_id)
        return render(request, 'announcements_edit.html',{'course':course,'announcement':announcement,'form':form})




# from django.shortcuts import render, get_object_or_404
# from django.views import generic
# from .models import Announcement
# from courses.models import Course

# # Create your views here.
# class AnnouncementView(generic.View):

#     def course_announcements(request, course_name):
#         course = get_object_or_404(Course, name=course_name)
#         return render(request, 'announcements.html', {'course': course})


#     def get_queryset(self):
#         return Announcement.objects.all()
