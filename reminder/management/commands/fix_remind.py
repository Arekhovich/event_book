from datetime import timedelta, datetime

from django.core.management import BaseCommand
from reminder.models import Event


class Command(BaseCommand):
    def handle(self, *args, **options):
        events = Event.objects.all()


        for e in events:
            date_time_event = datetime.combine(e.date_event, e.time_start)
            if e.type_of_remind_id == 1:
                e.remind = (timedelta(hours=1))
                e.time_remind = date_time_event - e.remind

            if e.type_of_remind_id == 2:
                e.remind = (timedelta(hours=2))
                e.time_remind = date_time_event - e.remind

        Event.objects.bulk_update(events, ['remind', 'time_remind'])