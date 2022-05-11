from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.db import models
from django.contrib import messages

from .models import CatalogItem, Shipment
from .forms import CatalogItemForm, ShipmentForm


class IndexView(View):
    def get(self, request):
        context = {
            'items': CatalogItem.objects.all(),
            'shipments': Shipment.objects.all()
        }
        return render(request, 'inventory/index.html', context)


class AddCatalogItemView(View):
    def get(self, request):
        context = {
            'form': CatalogItemForm()
        }
        return render(request, 'inventory/add-catalog-item.html', context)

    def post(self, request):
        form = CatalogItemForm(request.POST)
        if form.is_valid():
            CatalogItem.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
            )
            return redirect('inventory:index')
        else:
            return redirect('inventory:add-item')


class CatalogItemView(View):
    def get(self, request, id):
        existing = get_object_or_404(CatalogItem, id=id)
        context = {
            'item': existing,
            'form': CatalogItemForm(instance=existing)
        }
        return render(request, 'inventory/catalog-item.html', context)

    def post(self, request, id):
        print(request.POST)
        form = CatalogItemForm(request.POST)
        if form.is_valid():
            item = get_object_or_404(CatalogItem, id=id)
            if request.POST.get('action') == 'Update':
                item.name = form.cleaned_data.get('name')
                item.description = form.cleaned_data.get('description')
                item.save()
                messages.success(request, 'Item updated successfully')
                return redirect('inventory:item', id)
            elif request.POST.get('action') == 'Delete':
                try:
                    item.delete()
                    messages.success(
                        request, 'Item successfully deleted from catalog')
                    return redirect('inventory:index')
                except models.ProtectedError:
                    messages.error(
                        request, 'Cannot delete item from catalogue: Item exists in shipment')
                    return redirect('inventory:item', id)
            else:
                return redirect('inventory:item', id)
        else:
            return redirect('inventory:item', id)


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


class ShipmentView(View):
    def get(self, request, id):
        shipment = get_object_or_404(Shipment, id=id)
        context = {
            'item': shipment,
            'form': ShipmentForm(instance=shipment)
        }
        return render(request, 'inventory/shipment.html', context)

    def post(self, request, id):
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = get_object_or_404(Shipment, id=id)
            if request.POST.get('action') == 'Update':
                shipment.item = form.cleaned_data.get('item')
                shipment.date = form.cleaned_data.get('date')
                shipment.quantity = form.cleaned_data.get('quantity')
                shipment.save()
                messages.success(request, 'Shipment updated successfully')
                return redirect('inventory:shipment', id)
            elif request.POST.get('action') == 'Delete':
                shipment.delete()
                messages.success(request, 'Shipment deleted successfully')
                return redirect('inventory:index')
            else:
                return redirect('inventory:shipment', id)
        else:
            return redirect('inventory:shipment', id)
