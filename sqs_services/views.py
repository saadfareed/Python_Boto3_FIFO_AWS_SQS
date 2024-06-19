from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from sqs_services.utils.sqs_utils import send_to_sqs,retrieve_from_sqs,delete_from_sqs,get_queue_message_count
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
import external_interfacing_backend.settings as settings


@permission_classes([AllowAny])
class SqsGerminationViewSet(ViewSet):
    http_method_names = ['post', 'get']
    permission_classes = [AllowAny]

    def output_view(self, request):
        response = send_to_sqs(request.data,settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.GERMINATION_QUEUE_URL)
        return Response(response)

    @action(methods=['post'], detail=False, url_path='send-to-normal-sqs')
    def send_germination_to_sqs(self, request):
        return self.output_view(request=request)
    
    @action(methods=['get'], detail=False, url_path='retrieve-from-normal-sqs')
    def retrieve_germination_from_sqs(self,request):
        response = retrieve_from_sqs(settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.GERMINATION_QUEUE_URL)
        return Response(response)
    
    @action(methods=['post'], detail=False, url_path='delete-from-normal-sqs')
    def delete_germination_from_sqs(self,request):
        message = request.data.get('ReceiptHandle')
        response = delete_from_sqs(message,settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.GERMINATION_QUEUE_URL)
        return Response(response)

    @action(methods=['get'], detail=False, url_path='get-message-count-from-queue')
    def get_message_count_from_sqs(self, request):
        response = get_queue_message_count(settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.GERMINATION_QUEUE_URL)
        return Response(response)
    
    @action(methods=['get'], detail=False, url_path='get-message-count-from-dlq')
    def get_message_count_from_dlq_sqs(self, request):
        response = get_queue_message_count(settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.GERMINATION_DLQ_QUEUE_URL)
        return Response(response)


@permission_classes([AllowAny])
class SqsPlanetViewSet(ViewSet):
    http_method_names = ['post', 'get']
    permission_classes = [AllowAny]

    def output_view(self, request):
        response = send_to_sqs(request.data,settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.PLANET_IMAGERY_QUEUE_URL)
        return Response(response)

    @action(methods=['post'], detail=False, url_path='send-to-normal-sqs')
    def send_planet_imagery_to_sqs(self, request):
        return self.output_view(request=request)
    
    @action(methods=['get'], detail=False, url_path='retrieve-from-normal-sqs')
    def retrieve_planet_imagery_from_sqs(self,request):
        response = retrieve_from_sqs(settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.PLANET_IMAGERY_QUEUE_URL)
        return Response(response)
    
    @action(methods=['post'], detail=False, url_path='delete-from-normal-sqs')
    def delete_planet_imagery_from_sqs(self,request):
        message = request.data.get('ReceiptHandle')
        response = delete_from_sqs(message,settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.PLANET_IMAGERY_QUEUE_URL)
        return Response(response)
    
    @action(methods=['get'], detail=False, url_path='get-message-count-from-queue')
    def get_message_count_from_sqs(self, request):
        response = get_queue_message_count(settings.AWS_ACCESS_KEY,settings.AWS_SECRET_ACCESS_KEY,settings.PLANET_IMAGERY_QUEUE_URL)
        return Response(response)