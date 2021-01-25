from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from reminder.serializers import RegisterSerializer, UserSerializer


class MainPage(View):
    def page(self):
        return HttpResponse('Hello, user')

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })
