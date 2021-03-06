from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail
from reminder.models import Event, Country, CountryHoliday
import arrow
from ics import Calendar
import requests

@shared_task()
def remind_event():
    all_events = Event.objects.filter(notification=False)
    for every_event in all_events:
        if every_event.remind:
            timezone = tz = datetime.now() + timedelta(hours=3)
            if every_event.time_remind.timestamp() <= timezone.timestamp():
                subject = 'Вам направлено напоминание о событии'
                message = f'{every_event.user.username}, напоминаем Вам о следующем сохранненом событии. ' \
                          f'Событие: {every_event.event},' \
                          f'время начала: {every_event.time_start}, ' \
                          f'время окончания: {every_event.time_finish}.'
                send_mail(
                    subject,
                    message,
                    'e.orechovich92@gmail.com',
                    [every_event.user.email]
                )
                Event.objects.filter(id=every_event.id).update(notification=True)
                print(every_event.id, 'ok')

@shared_task()
def update_holidays():
    CountryHoliday.objects.all().delete
    all_countries = Country.objects.all()
    error = []
    for one_country in all_countries:
        try:
            url = "https://www.officeholidays.com/ics-clean/" + one_country.name_country
            holidays = list(Calendar(requests.get(url).text).events)
            for h in holidays:
                CountryHoliday.objects.create(
                    country_id=one_country.id,
                    holidays=h.name,
                    holiday_begin=arrow.get(h.begin).format("YYYY-MM-DD"),
                    holiday_end=arrow.get(h.end).format("YYYY-MM-DD"),
                )
        except Exception:
            error.append(one_country.name_country)
            continue