from django.urls import path
from .views import *

app_name = 'notice'

urlpatterns = [
    path('', notice_list, name='notice_list'),
    path('<int:pk>/', notice_detail, name='notice_detail'),
    path('new/', notice_new, name='notice_new'),
    path('<int:pk>/edit/', notice_edit, name='notice_edit'),
    path('<int:pk>/delete/', notice_delete, name='notice_delete'),
]