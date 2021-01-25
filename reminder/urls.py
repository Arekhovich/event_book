from django.urls import path

from reminder.views import MainPage, RegisterAPI

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path("", MainPage.as_view(), name="the-main-page"),
]