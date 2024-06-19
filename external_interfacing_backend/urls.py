"""
URL configuration for external_interfacing_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

class Home(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    renderer_classes = [JSONRenderer,]

    def get(self, request):
        return Response("External API Server Running")


urlpatterns = [
    path('', Home.as_view(), name='home_view'),
    path('admin/', admin.site.urls),
    path('email-service/', include("email_services.urls")),
    path('external-interfacing-core/', include("external_interfacing_core.urls")),
    path('sqs-services/', include("sqs_services.urls"))
]
