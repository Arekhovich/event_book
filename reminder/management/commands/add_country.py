from django.core.management.base import BaseCommand
from reminder.models import Country
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Command(BaseCommand):
    def handle(self, *args, **options):
        html = urlopen("https://www.officeholidays.com/countries").read().decode('utf-8')
        pars_page = str(html)
        soup = BeautifulSoup(pars_page, 'html.parser')
        all_countries = []
        for link in soup.find_all('a', href=True):
            if 'countries/' in link['href']:
                country = link['href'].split('/countries/')[1]
                all_countries.append(country)

        instances = [
            Country(name_country=one_country)
            for one_country in all_countries
        ]

        Country.objects.bulk_create(instances)