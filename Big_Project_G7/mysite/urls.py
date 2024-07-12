# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    
    path('chatgpt/',include('chatgpt.urls')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('ticket/', include('ticket.urls')),
    path('exhibition/', include(('exhibition.urls', 'exhibition'), namespace='exhibition')),

    # 1기 전시회
    path('layout1/', views.layout1, name='layout1'),

    # 부스 프로그램 예약 관련
    path('booth_program/', include(('booth_program.urls', 'booth_program'), namespace='booth_program')),
    path('reservation/<str:booth_id>/', views.reservation, name='reservation'),
    path('confirmation/', views.confirmation, name='confirmation'),
    # path('change_permission/', views.change_permission, name='change_permission'),
    path('program_open/', views.program_open, name='program_open'),

    
    #AIVEX/info
    path('notice/', include('notice.urls')),
    path('FAQ/', views.FAQlist, name='faq_page'),
    path('AIVEX/about/', views.about, name='aivexabout'), # AIVEX/about/
    path('AIVEX/hall/', views.aivexhall, name='aivexhall'), #former aivexhall, 홀 정보

    
    # etc
    path('mypage/', views.mypage, name='mypage'), #마이페이지 사용하는지?
    path('reserve/', include('reserve_hall.urls', namespace='reserve_hall')), #사용유무 확실x
    path('reserve_exhib/', views.reserve_exhib, name='reserve_exhib'), #예약하기 버튼 어디로 매핑되는지?
    path('edit_booth/', views.edit_booth_view, name='edit_booth'), #template x
    path('layout5/', views.create_exhibition, name='layout5'), #template x
    
    path('program_choice/', views.program_choice, name='program_choice'),
    # path('program_manage/', views.program_manage, name='program_manage'),
    # path('programs/', include('programs.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)