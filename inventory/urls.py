from django.urls import path

from .views import IndexView, AddCatalogEntryView, AddInventoryItemView, CatalogEntryView, InventoryItemView

app_name='inventory'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-catalog-entry/', AddCatalogEntryView.as_view(), name='add-catalog-entry'),
    path('add-inventory-item/', AddInventoryItemView.as_view(), name='add-item'),
    path('catalog-entry/<int:id>', CatalogEntryView.as_view(), name='catalog-entry'),
    path('inventory-items/<int:id>', InventoryItemView.as_view(), name='item'),
]
