from django.urls import path, include

from reminder.views import MainPage, RegisterAPI, CreateEvent, CreateToken, YourEvents, YourHolidays, YourMonthEvents

urlpatterns = [
    path('holidays/', YourHolidays.as_view()),
    path('yourmonthevents/', YourMonthEvents.as_view()),
    path('addevent', CreateEvent.as_view(), name='create-event'),
    path('yourevents', YourEvents.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('register', RegisterAPI.as_view(), name='register'),
    path('create_token', CreateToken.as_view(), name='create-token'),
    path("", MainPage.as_view(), name="the-main-page"),
]