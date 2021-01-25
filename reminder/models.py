from django.db import models
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    name_country = models.TextField()

    def __str__(self):
        return self.name_country


class MyUser(AbstractUser):
   country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True,
                                  blank=True, related_name='country_user',
                                  verbose_name='Страна')
