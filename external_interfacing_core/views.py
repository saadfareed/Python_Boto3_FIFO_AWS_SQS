from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.template.loader import render_to_string

@permission_classes([AllowAny])
class HomeView(APIView):
    http_method_names = ['get']
    permission_classes = [AllowAny]

    def output_view(self, request):
        return Response({'status': 'success', 'message': "Test"})

    def get(self, request):
        return self.output_view(request=request)