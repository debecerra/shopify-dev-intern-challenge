from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Item, Shipment

class IndexView(View):
    def get(self, request):
        context = {
            'items': Item.objects.all(),
            'shipments': Shipment.objects.all()
        }
        return render(request, 'inventory/index.html', context)

