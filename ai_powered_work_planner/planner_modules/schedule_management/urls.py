from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_view, name='schedule'),
    path('monthly/', views.monthly_view, name='monthly_schedule'),
    path('add/', views.create_shift_view, name='add_shift'),
    path('edit/<int:shift_id>/', views.update_shift_view, name='edit_shift'),
    path('delete/<int:shift_id>/', views.delete_shift_view, name='delete_shift'),
    path('availability/', views.availability_view, name='availability'),
]