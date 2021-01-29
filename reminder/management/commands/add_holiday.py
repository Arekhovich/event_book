import arrow
from django.core.management import BaseCommand
from reminder.models import Country, CountryHoliday
from ics import Calendar
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
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
