from django.contrib import admin

from .models import CatalogEntry, InventoryItem, Country, City, Warehouse

admin.site.register(CatalogEntry)
admin.site.register(InventoryItem)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Warehouse)
