# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatgpt/',include('chatgpt.urls')),
    path('login/', views.login_view, name='login'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('mypage/', views.mypage, name='mypage'),
    path('reserve_exhib/', views.reserve_exhib, name='reserve_exhib'),
    path('ticket/', include('ticket.urls')),
    path('layout1/', views.layout1, name='layout1'),
    path('layout2/', views.layout2, name='layout2'),
    path('layout3/', views.layout3, name='layout3'),
    path('layout4/', views.FAQlist, name='layout4'),
    path('layout5/', views.create_exhibition, name='layout5'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('edit_booth/', views.edit_booth_view, name='edit_booth'),
    path('reservation/<str:booth_id>/', views.reservation, name='reservation'),
    path('confirmation/', views.confirmation, name='confirmation'),
    # path('change_permission/', views.change_permission, name='change_permission'),
    path('program_open/', views.program_open, name='program_open'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # original
    # path('booth_program/', include('booth_program.urls')),
    
    # added
    path('booth_program/', include(('booth_program.urls', 'booth_program'), namespace='booth_program')),
    
    path('exhibition/', include(('exhibition.urls', 'exhibition'), namespace='exhibition')),
    path('notice/', include('notice.urls')),
    path('FAQ/', views.FAQlist, name='faq_page'),
    path('reserve/', include('reserve_hall.urls', namespace='reserve_hall')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)