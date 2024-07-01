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