from django.conf.urls import include
from django.urls import path, re_path

from email_services import views
from rest_framework.routers import DefaultRouter

app_name = 'email_service'

router = DefaultRouter()
# router.register(r'send-germination-report/', views.SendGerminationReportView, basename='send_germination_report')

# URL PATTERNS
urlpatterns = [
    path('send-germination-report/', views.SendGerminationReportView.as_view()),
    path('email-notification/', views.SendEmailNotificationView.as_view()),
    re_path(r'', include(router.urls))
]
