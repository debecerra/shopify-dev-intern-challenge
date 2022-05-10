from django.contrib import admin

from .models import Item, Shipment

admin.site.register(Item)
admin.site.register(Shipment)