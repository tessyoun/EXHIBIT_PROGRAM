from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'exhibition'
urlpatterns = [
    path('list/', views.exhibition_list, name='exhibition_list'), # 전시회 목록
    path('list/<str:date>/', views.exhibition_list_json, name='exhibition_list_json'), # 전시회 목록
    path('create_exhibition/', views.create_exhibition, name='create_exhibition'),
    # path('change_permission/', views.change_perm, name='change_perm'),
    path('update/', views.update_booths, name='update_booths'),
    path('booth_list/', views.booth_list, name='booth_list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
