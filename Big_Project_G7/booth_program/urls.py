# booth_program/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('program_open/', views.program_open, name='program_open'),
]
