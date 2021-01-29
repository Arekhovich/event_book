from django.contrib import admin

from .models import MyUser, Country, TypeReminder

admin.site.register(MyUser)
admin.site.register(Country)
admin.site.register(TypeReminder)
