from django.contrib import admin
from .models import *

class PostExhibition(admin.ModelAdmin):
    list_display = ['group', 'bname', 'bcat']
    list_display_links = ['group']
    list_filter = ['bcat']
    search_fields = ['group', 'bname', 'bcat']
    ordering = ['group']
    
admin.site.register(exbooth_1st, PostExhibition)
admin.site.register(exbooth_2nd, PostExhibition)
admin.site.register(exbooth_3rd, PostExhibition)
admin.site.register(exbooth_4th, PostExhibition)
admin.site.register(ImageUpload)

class PostExhibition(admin.ModelAdmin):
    list_display = ['exhibition_name', 'host_id', 'hall']
    list_display_links = ['exhibition_name']
    ordering = ['start_date']
    
admin.site.register(Exhibition, PostExhibition)