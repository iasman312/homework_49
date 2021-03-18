from django.contrib import admin
from .models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created_at', 'updated_at']
    list_filter = ['summary']
    search_fields = ['summary']
    fields = ['summary', 'statuses', 'types', 'description']
    readonly_fields = ['created_at', 'updated_at', 'id']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)

