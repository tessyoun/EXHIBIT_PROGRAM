from django.urls import path
from . import views

app_name = 'reserve_hall' 

urlpatterns = [
    path('hall/<str:hall_name>/', views.reserve_hall, name='reserve_hall'),
    path('success/', views.success, name='success'),
]
