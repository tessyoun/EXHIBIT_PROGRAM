from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('create_exhibition/', views.create_exhibition, name='create_exhibition'),
    path('change_permission/', views.change_perm, name='change_perm'),
    path('update/', views.update_booths, name='update'),
    path('booth_list/', views.booth_list, name='booth_list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
