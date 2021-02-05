from datetime import date
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import auth
from django.contrib.auth import login
from reminder.models import Event, CountryHoliday
from reminder.serializers import RegisterSerializer, UserSerializer, EventSerializer, HolidaySerializer, \
    GroupByDayEventSerializer


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data},
                        status=status.HTTP_201_CREATED)


class CreateToken(APIView):

    def post(self, request):
        login = request.data.get('login')
        pwd = request.data.get('pwd')
        email = request.data.get('email')
        user = auth.authenticate(request, password=pwd, email=email)
        if user is not None:
            token, flag = Token.objects.get_or_create(user=user)
            subject = "Вам направлен токен"
            send_mail(subject=subject,
                      message=token.__str__(),
                      from_email='e.orechovich92@gmail.com',
                      recipient_list=[email])
            return Response({'token': token.__str__()}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    def post(self, request):
        user = auth.authenticate(
            request,
            email=request.data['email'],
            password=request.data['password']
        )
        if user is not None:
            login(request, user)
            return Response({}, status=status.HTTP_201_CREATED)
        return Response("this user is not exists", status=status.HTTP_400_BAD_REQUEST)


class CreateEvent(ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class YourEvents(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        events = Event.objects.filter(user_id=self.request.user.id)
        today_events = events.filter(date_event=date.today())
        return today_events


class YourMonthEvents(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GroupByDayEventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        events = Event.objects.filter(
            user_id=self.request.user.id,
            date_event__month=date.today().month
        )
        days = events.order_by('date_event').values('date_event').distinct()
        for day in days:
            events_in_day = [
                f'{e.event}: {e.date_event} с {e.time_start} по {e.time_finish}'
                for e in Event.objects.filter(date_event=day['date_event'])
            ]
            day['event'] = events_in_day
        return days


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
