from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from datetime import date
from django.template.loader import render_to_string
from email_services.utils.email_utils import send_email,send_notification


@permission_classes([AllowAny])
class SendGerminationReportView(APIView):
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def output_view(self, request):
        userEmails = request.data.get('UserEmails',[])

        request.data['CurrentDate'] = request.data.get('CurrentDate', date)
        request.data['FarmName'] = request.data.get('FarmName')
        request.data['FlightDate'] = request.data.get('FlightDate')
        request.data['CropUniqueNo'] = request.data.get('CropUniqueNo')
        request.data['CropName'] = request.data.get('CropName')
        request.data['TotalPlants'] = request.data.get('TotalPlants')
        request.data['AvgPlantsPerAcre'] = request.data.get('AvgPlantsPerAcre')

        response = send_email("Latest Germination Report", render_to_string('germination_report_email.html', request.data), userEmails)
        return Response(response)

    def post(self, request):
        return self.output_view(request)
    

@permission_classes([AllowAny])
class SendEmailNotificationView(APIView):
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def output_view(self, request):
        userEmail = request.data.get('userEmail')
        messageList = request.data.get('messageList',[])
        response = send_notification("You have a latest Agrilift Notifications", render_to_string('email_notification.html', {"messages":messageList}), userEmail)
        return Response(response)

    def post(self, request):
        return self.output_view(request)