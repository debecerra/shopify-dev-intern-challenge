from django.contrib import admin

from .models import CatalogItem, Shipment

admin.site.register(CatalogItem)
admin.site.register(Shipment)