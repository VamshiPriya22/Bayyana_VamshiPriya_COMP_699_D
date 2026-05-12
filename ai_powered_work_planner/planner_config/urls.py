from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # =========================
    # DJANGO ADMIN
    # =========================
    path('admin/', admin.site.urls),

    # =========================
    # USER MANAGEMENT (Auth + Dashboard)
    # =========================
    path('', include('planner_modules.user_management.urls')),

    # =========================
    # JOB MANAGEMENT
    # =========================
    path('jobs/', include('planner_modules.job_management.urls')),

    # =========================
    # SCHEDULE MANAGEMENT
    # =========================
    path('schedule/', include('planner_modules.schedule_management.urls')),

    # =========================
    # AI ENGINE (⚠️ SAFE CHECK)
    # =========================
    # Only keep this if urls.py exists inside ai_planner_engine
    # Otherwise comment it
    path('ai/', include('planner_modules.ai_planner_engine.urls')),

    # =========================
    # REPORT MANAGEMENT (⚠️ SAFE CHECK)
    # =========================
    path('reports/', include('planner_modules.report_management.urls')),

    # =========================
    # SYSTEM ADMIN PANEL
    # =========================
    path('system/', include('planner_modules.system_admin.urls')),
]


# =========================
# STATIC & MEDIA (DEV ONLY)
# =========================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)