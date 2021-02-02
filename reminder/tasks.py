from datetime import datetime
from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import send_mail
from reminder.models import Event


@periodic_task(run_every=crontab(hour="*/1"))
def remind_event():
    all_events = Event.objects.filter(notification=False)
    for every_event in all_events:
        if every_event.remind:
            if every_event.time_remind <= datetime.now():
                subject = 'Вам направлено напоминание о событии'
                message = f'{every_event.user}, напоминаем Вам о следующем сохранненом событии. ' \
                          f'Событие: {every_event.event},' \
                          f'время начала: {every_event.time_start}, ' \
                          f'время окончания: {every_event.time_finish}.'
                mail_sent = send_mail(subject,
                                      message,
                                      'e.orechovich92@gmail.com',
                                      [every_event.user.email])
                Event.objects.filter(id=every_event.id).update(notification=True)
                print(every_event.id, 'ok')
