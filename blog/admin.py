from django.contrib.admin.models import LogEntry
from django.contrib import admin
from .models import Post

admin.site.register(Post)

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("action_time","user","content_type","object_id","object_repr","action_flag","change_message",)
    list_filter = ("action_flag", "content_type", "user")
    search_fields = ("object_id", "object_repr")

admin.site.register(LogEntry, LogEntryAdmin)