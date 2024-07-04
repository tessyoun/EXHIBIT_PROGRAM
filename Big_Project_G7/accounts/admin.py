from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'name', 'phone_number']
    list_display_links = ['user']
    list_filter = ['user_type']
    search_fields = ['user', 'name']
    
admin.site.register(Profile, PostAdmin)

