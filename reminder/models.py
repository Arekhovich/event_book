from django.db import models
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    name_country = models.TextField()

    def __str__(self):
        return self.name_country


class MyUser(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True,
                                blank=True, related_name='country_user',
                                verbose_name='Страна'
                                )
    email = models.EmailField(unique=True, blank=False)


class TypeReminder(models.Model):
    reminder = models.TextField()

    def __str__(self):
        return self.reminder


class CountryHoliday(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True,
                                blank=True, related_name='country_holiday',
                                )
    holidays = models.TextField(null=True)
    holiday_begin = models.DateField(null=True)
    holiday_end = models.DateField(null=True)

class Event(models.Model):
    event = models.TextField(max_length=2000, verbose_name='Событие')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_event')
    date_event = models.DateField()
    time_start = models.TimeField()
    time_finish = models.TimeField()
    type_of_remind = models.ForeignKey(TypeReminder, on_delete=models.CASCADE, related_name='reminder_event')
