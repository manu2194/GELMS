from django.contrib import admin
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','cid',)

admin.site.register(Course, CourseAdmin)
