from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('create_exhibiton/', views.create_exhibition, name='create_exhibition'),
    path('change_permission/', views.change_perm, name='change_perm'),

]
