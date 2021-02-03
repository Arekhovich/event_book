from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
import datetime


class Country(models.Model):
    name_country = models.TextField()

    def __str__(self):
        return self.name_country


class MyUser(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True,
                                blank=True, related_name='country_user',
                                verbose_name='Страна'
                                )
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, blank=False)
    REQUIRED_FIELDS = []


class CountryHoliday(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True,
                                blank=True, related_name='country_holiday',
                                )
    holidays = models.TextField(null=True)
    holiday_begin = models.DateField(null=True)
    holiday_end = models.DateField(null=True)


class Event(models.Model):
    TYPE_REMIND = [
        ((timedelta(hours=1)), 'За час'),
        ((timedelta(hours=2)), 'За 2 часа'),
        ((timedelta(hours=4)), 'За 4 часа'),
        ((timedelta(days=1)), 'За день'),
        ((timedelta(weeks=1)), 'За неделю'),
    ]
    event = models.TextField(max_length=2000, verbose_name='Событие')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_event')
    date_event = models.DateField()
    time_start = models.TimeField()
    time_finish = models.TimeField(default='23:59:59')
    remind = models.CharField(max_length=30, choices=TYPE_REMIND, null=True, blank=True)
    time_remind = models.DateTimeField(null=True, blank=True)
    notification = models.BooleanField(default=False)

    def __str__(self):
        return self.event

    def save(self, **kwargs):
        if self.remind:
            datetime_event = datetime.datetime.combine(self.date_event, self.time_start)
            self.time_remind = datetime_event - self.remind
        super().save(**kwargs)
