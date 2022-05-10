from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item, Shipment
from .forms import ItemForm, ShipmentForm


class IndexView(View):
    def get(self, request):
        context = {
            'items': Item.objects.all(),
            'shipments': Shipment.objects.all()
        }
        return render(request, 'inventory/index.html', context)


class AddItemView(View):
    def get(self, request):
        context = {
            'form': ItemForm()
        }
        return render(request, 'inventory/add-item.html', context)

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            Item.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
            )
            return redirect('inventory:index')
        else:
            return redirect('inventory:add-item')


class AddShipmentView(View):
    def get(self, request):
        context = {
            'form': ShipmentForm()
        }
        return render(request, 'inventory/add-shipment.html', context)

    def post(self, request):
        form = ShipmentForm(request.POST)
        if form.is_valid():
            Shipment.objects.create(
                item=form.cleaned_data.get('item'),
                date=form.cleaned_data.get('date'),
                quantity=form.cleaned_data.get('quantity'),
            )
            return redirect('inventory:index')
        else:
            return redirect('inventory:add-shipment')
