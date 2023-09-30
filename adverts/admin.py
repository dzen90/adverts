from django.contrib import admin

# Register your models here.
from .models import Advert

class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'number_of_rooms', 'area', 'price')

admin.site.register(Advert, AdvertAdmin)