from django.urls import path
from planner_modules.user_management.views import dashboard_view

urlpatterns = [
    path('insights/', dashboard_view, name='ai_insights'),
]