from datetime import date
from .tasks import remind_event
from django.core.mail import send_mail
from django.db.models.functions import TruncDate, TruncDay
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import auth
from reminder.models import Event, MyUser, CountryHoliday
from reminder.serializers import RegisterSerializer, UserSerializer, EventSerializer, HolidaySerializer, \
    MonthEventSerializer, GroupByDayEventSerializer


class MainPage(View):
    def page(self):
        return HttpResponse('Hello, user')


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data},
                        status=status.HTTP_201_CREATED)


class CreateEvent(ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateToken(APIView):

    def post(self, request):
        login = request.data.get('login')
        pwd = request.data.get('pwd')
        email = request.data.get('email')
        user = auth.authenticate(request, username=login, password=pwd, email=email)
        if user is not None:
            token, flag = Token.objects.get_or_create(user=user)
            subject = "Вам направлен токен"
            send_mail(subject=subject,
                      message=token.__str__(),
                      from_email='e.orechovich92@gmail.com',
                      recipient_list=[email])
            return Response({'token': token.__str__()}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


class YourEvents(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MonthEventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        events = Event.objects.filter(user_id=self.request.user.id)
        today_events = events.filter(date_event=date.today())
        return today_events


class YourMonthEvents(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GroupByDayEventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        events = Event.objects.filter(user_id=self.request.user.id)
        if self.request.GET['date'].split('-')[0]:
            if self.request.GET['date'].split('-')[1]:
                self.request.GET['date'].split('-')[2]

        day_ev = events.order_by('date_event')
        return day_ev

    # def get(self, request):
    #     events_for_day = self.get_queryset()









class YourHolidays(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HolidaySerializer
    queryset = CountryHoliday.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["holiday_begin"]
    filter_fields = ('holiday_begin', 'holidays')

    def get_queryset(self):
        holidays = CountryHoliday.objects.filter(
            country=self.request.user.country_id
        )
        return holidays
