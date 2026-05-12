from django.urls import path
from . import views

urlpatterns = [
    # 🔥 FIXED NAME (IMPORTANT)
    path('', views.job_list_view, name='job_list'),

    # CREATE
    path('add/', views.create_job_view, name='add_job'),

    # UPDATE
    path('edit/<int:job_id>/', views.update_job_view, name='edit_job'),

    # DELETE
    path('delete/<int:job_id>/', views.delete_job_view, name='delete_job'),
]