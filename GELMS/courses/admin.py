from django.contrib import admin
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','domain',)
    filter_horizontal = ('students','graders','teachers')


admin.site.register(Course, CourseAdmin)
