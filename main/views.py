import base64

from django.shortcuts import render
from rest_framework.views import APIView
from main.serializers import UserSerializer
from rest_framework.response import Response
# Create your views here.
from rest_framework.exceptions import ValidationError
from main.models import User
from main.forms import FileForm

class SignUpView(APIView):

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response({"access_token": "token", "refresh_token": "refresh"})
        except Exception as e:
            raise e


def get_username_and_password_from_header(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        try:
            token_type, _, credentials = auth_header.partition(' ')
            secret = base64.b64decode(credentials)
            username, password = secret.decode().split(":")
        except:
            raise ValidationError('invalid jwt')

        return username, password


class LogInView(APIView):

    def post(self, request):
        try:
            username, password = get_username_and_password_from_header(request=request)
            user = User.objects.get(username=username)
            if user.password != password:
                raise ValidationError('invalid password')
            return Response({"access_token": "token", "refresh_token": "refresh"})
        except Exception as e:
            raise e



class ConverterView(APIView):
    def post(self,request):
        request = request
        form = FileForm(request.POST,request.FILES)
        print(request)

