from django.urls import path, include

from reminder.views import MainPage, RegisterAPI, CreateEvent, CreateToken

urlpatterns = [
    path('addevent', CreateEvent.as_view(), name='create-event'),
    path('rest-auth/', include('rest_auth.urls')),
    path('register', RegisterAPI.as_view(), name='register'),
    path('create_token', CreateToken.as_view()),
    path("", MainPage.as_view(), name="the-main-page"),
]