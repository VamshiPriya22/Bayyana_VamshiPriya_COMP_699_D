from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('retrain/', views.retrain_model_view, name='retrain_model'),
    path('update-rules/', views.update_rules_view, name='update_rules'),
]