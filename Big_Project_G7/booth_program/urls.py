from django.urls import path
from . import views

app_name = 'booth_program'

urlpatterns = [
    path('program_open/', views.program_open, name='program_open'),
    path('program_manage/', views.program_manage, name='program_manage'),
    path('program_edit/<int:program_id>/', views.program_edit, name='program_edit'),
    path('reserve/<int:booth_id>/', views.reserve_booth, name='reserve_booth'),
    path('check_program/<str:company_name>/', views.check_program, name='check_program'),
    path('submit_reservation/', views.submit_reservation, name='submit_reservation'),
    path('reservation_check/', views.reservation_check, name='reservation_check'),
    path('reservation_check/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('reservation_check/edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('program_choice/', views.program_choice, name='program_choice'),
]

