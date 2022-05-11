from django.contrib import admin

from .models import CatalogEntry, InventoryItem

admin.site.register(CatalogEntry)
admin.site.register(InventoryItem)