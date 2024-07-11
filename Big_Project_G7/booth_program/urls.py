from django.urls import path
from . import views

app_name = 'booth_program'

urlpatterns = [
    path('program_open/', views.program_open, name='program_open'),
    path('program/manage/', views.program_manage, name='program_manage'),
    path('reserve/<int:booth_id>/', views.reserve_booth, name='reserve_booth'),
    path('check_program/<str:company_name>/', views.check_program, name='check_program'),
    path('submit_reservation/', views.submit_reservation, name='submit_reservation'),
]
