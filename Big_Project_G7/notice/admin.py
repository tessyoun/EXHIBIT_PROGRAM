from django.contrib import admin
from .models import Notice

# Register your models here.
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_time', 'update_time')