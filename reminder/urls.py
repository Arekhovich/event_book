from django.urls import path, include
from reminder.views import RegisterAPI, CreateEvent, CreateToken, YourEvents, YourHolidays, YourMonthEvents, LoginUser

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('create_token', CreateToken.as_view(), name='create-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('holidays/', YourHolidays.as_view()),
    path('addevent', CreateEvent.as_view(), name='create-event'),
    path('yourmonthevents/', YourMonthEvents.as_view()),
    path('loginuser/', LoginUser.as_view()),
    path('yourevents/', YourEvents.as_view()),
]