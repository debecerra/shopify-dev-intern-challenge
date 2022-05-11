from django.urls import path

from .views import IndexView, AddCatalogItemView, AddShipmentView, CatalogItemView, ShipmentView

app_name='inventory'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-items/', AddCatalogItemView.as_view(), name='add-item'),
    path('add-shipment/', AddShipmentView.as_view(), name='add-shipment'),
    path('items/<int:id>', CatalogItemView.as_view(), name='item'),
    path('shipments/<int:id>', ShipmentView.as_view(), name='shipment'),
]
