from datetime import datetime
from django.core.mail import send_mail
from reminder.models import Event
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
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
