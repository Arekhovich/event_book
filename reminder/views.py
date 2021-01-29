from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import auth

from reminder.models import Event, MyUser
from reminder.serializers import RegisterSerializer, UserSerializer, EventSerializer


class MainPage(View):
    def page(self):
        return HttpResponse('Hello, user')

class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": Token.objects.get_or_create(user=user)[1]
        })

class CreateEvent(ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class CreateToken(APIView):
    def post(self, request):
        login = request.data.get('login')
        pwd = request.data.get('pwd')
        user = auth.authenticate(request, username=login, password=pwd)
        if user is not None:
            token, flag = Token.objects.get_or_create(user=user)
            return Response({'token': token.__str__()}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

