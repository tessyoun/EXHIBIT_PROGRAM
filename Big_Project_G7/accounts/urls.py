# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    # path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update_profile, name='update'),
    path('info/', views.info, name='info'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/update', views.update, name='update'),
]
