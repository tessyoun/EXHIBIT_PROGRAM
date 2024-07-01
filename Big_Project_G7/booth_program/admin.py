# booth_program/admin.py
from django.contrib import admin
from .models import Booth, Program, Reservation

admin.site.register(Booth)
admin.site.register(Program)
admin.site.register(Reservation)
