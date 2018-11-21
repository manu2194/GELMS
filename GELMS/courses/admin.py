from django.contrib import admin
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','cid',)
    filter_horizontal = ('students','grader','teacher')

admin.site.register(Course, CourseAdmin)
