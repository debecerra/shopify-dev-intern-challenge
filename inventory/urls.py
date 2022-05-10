from django.urls import path

from .views import IndexView, AddItemView, AddShipmentView

app_name='inventory'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-items/', AddItemView.as_view(), name='add-item'),
    path('add-shipment/', AddShipmentView.as_view(), name='add-shipment'),
]
