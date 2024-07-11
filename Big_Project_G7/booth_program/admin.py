# booth_program/admin.py
from django.contrib import admin
from .models import Program, BoothProgramReservation, ReservationTime

admin.site.register(Program)
admin.site.register(BoothProgramReservation)
admin.site.register(ReservationTime)