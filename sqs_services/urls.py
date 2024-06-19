from django.conf.urls import include
from django.urls import path, re_path

from sqs_services import views
from rest_framework.routers import DefaultRouter

app_name = 'sqs_services'

router = DefaultRouter()
router.register(r'germination', views.SqsGerminationViewSet, basename='germination')
router.register(r'planet', views.SqsPlanetViewSet, basename='planet')

# URL PATTERNS
urlpatterns = [
    re_path(r'', include(router.urls))
]
