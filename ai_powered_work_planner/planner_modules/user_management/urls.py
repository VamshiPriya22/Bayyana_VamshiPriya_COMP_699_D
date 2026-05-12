from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('reset-password/', views.reset_password_view, name='reset_password'),

    path('privacy/', views.privacy_view, name='privacy'),
    path('accept-terms/', views.accept_terms_view, name='accept_terms'),
]