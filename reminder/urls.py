from django.urls import path, include, re_path
from reminder.views import RegisterAPI, CreateEvent, CreateToken, YourEvents, YourHolidays, YourMonthEvents, LoginUser

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('create_token', CreateToken.as_view(), name='create-token'),
    path('loginuser', LoginUser.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    re_path(r'^[-\w]+/'),
    path('holidays', YourHolidays.as_view()),
    path('addevent', CreateEvent.as_view(), name='create-event'),
    path('yourmonthevents', YourMonthEvents.as_view()),
    path('yourevents', YourEvents.as_view()),
]
