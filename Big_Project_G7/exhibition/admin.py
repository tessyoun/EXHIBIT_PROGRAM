from django.contrib import admin
from .models import *

class PostExhibition(admin.ModelAdmin):
    list_display = ['company_name', 'booth_name', 'booth_category']
    list_display_links = ['company_name']
    list_filter = ['booth_category']
    search_fields = ['company_name', 'booth_name', 'booth_category']
    ordering = ['company_name']
    
admin.site.register(Booth_Info, PostExhibition)
admin.site.register(ImageUpload)

class PostExhibition(admin.ModelAdmin):
    list_display = ['exhibition_name', 'host_id', 'hall']
    list_display_links = ['exhibition_name']
    ordering = ['start_date']
    
admin.site.register(Exhibition, PostExhibition)