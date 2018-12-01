from django.contrib import admin
from tools.models import Tool


class ToolAdmin(admin.ModelAdmin):
    exclude = ['status']
    list_display = ('name','get_course_name','get_course_domain')

    def get_course_name(self, instance):
        return instance.course.name
    get_course_name.short_description = 'Course'

    def get_course_domain(self, instance):
        return instance.course.domain
    get_course_domain.short_description = 'Domain'

admin.site.register(Tool, ToolAdmin)
