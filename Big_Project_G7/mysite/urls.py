# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatgpt/',include('chatgpt.urls')),
    path('login/', views.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('mypage/', views.mypage, name='mypage'),
    path('layout1/', views.layout1, name='layout1'),
    path('layout2/', views.layout2, name='layout2'),
    path('layout3/', views.layout3, name='layout3'),
    path('layout4/', views.layout4, name='layout4'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('edit_booth/', views.edit_booth_view, name='edit_booth'),
    path('reservation/', views.reservation, name='reservation'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('memberinfo/', views.memberinfo_view, name='memberinfo'),
    path('boothinfo/', views.boothinfo_view, name='boothinfo'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)