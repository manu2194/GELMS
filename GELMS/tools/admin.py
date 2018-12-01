from django.contrib import admin
from tools.models import Tool


class ToolAdmin(admin.ModelAdmin):
    exclude = ['status']

admin.site.register(Tool, ToolAdmin)
