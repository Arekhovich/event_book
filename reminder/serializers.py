from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer

from reminder.models import MyUser, Event, CountryHoliday


class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'country')


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'password', 'country')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['username'],
                                          email=validated_data['email'],
                                          password=validated_data['password'],
                                          country=validated_data['country'])

        return user


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class HolidaySerializer(ModelSerializer):
    class Meta:
        model = CountryHoliday
        fields = ('holidays', 'holiday_begin', 'holiday_end',)