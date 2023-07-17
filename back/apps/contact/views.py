

from rest_framework import permissions
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.views import APIView
from .models import EmailModel
from django.conf import settings
# views.py
activecampaing_url = settings.ACTIVE_CAMPAING_URL
activecampaing_key = settings.ACTIVE_CAMPAING_KEY
from django.core.mail import send_mail


class EmailView(APIView):
    def post(self, request, format=None):
        data = self.request.data

        try:
            return Response({'succes':'Email send'})
        except:
            return Response({'error':'Message failed to be send'})
