from django.contrib import admin

from .models import MyUser, Country

admin.site.register(MyUser)
admin.site.register(Country)

