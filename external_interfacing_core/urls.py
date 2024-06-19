from django.conf.urls import include
from django.urls import path, re_path

from external_interfacing_core import views
from rest_framework.routers import DefaultRouter

app_name = 'external_interfacing_core'

router = DefaultRouter()

# URL PATTERNS
urlpatterns = [
    path('', views.HomeView.as_view()),
    re_path(r'', include(router.urls)),
]
