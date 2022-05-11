from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.db import models
from django.contrib import messages

from .models import CatalogEntry, InventoryItem
from .forms import CatalogEntryForm, InventoryItemForm


class IndexView(View):
    """ View to display on index of Inventory application
    """

    def get(self, request):
        """ Displays list of all catalog entries and inventory items.

        @param request: the HTTP request received by the server
        """

        context = {
            'catalog': CatalogEntry.objects.all(),
            'inventory': InventoryItem.objects.all()
        }
        return render(request, 'inventory/index.html', context)


class AddCatalogEntryView(View):
    def get(self, request):
        """ Displays form for creating a new catalog entry.

        @param request: the HTTP request received by the server
        """

        context = {
            'form': CatalogEntryForm()
        }
        return render(request, 'inventory/add-catalog-entry.html', context)

    def post(self, request):
        """ Creates a new catalog entry.

        @param request: the HTTP request received by the server
        """

        form = CatalogEntryForm(request.POST)
        if form.is_valid():
            CatalogEntry.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
            )
            return redirect('inventory:index')
        else:
            return redirect('inventory:add-catalog-entry')


class CatalogEntryView(View):
    def get(self, request, id):
        """ Displays single catalog entry with the option to edit or delete the entry.

        @param request: the HTTP request received by the server
        @param id: the id of the catalog entry
        """

        # get catalog entry and prepopulate form fields with entry
        existing = get_object_or_404(CatalogEntry, id=id)
        context = {
            'item': existing,
            'form': CatalogEntryForm(instance=existing)
        }
        return render(request, 'inventory/catalog-entry.html', context)

    def post(self, request, id):
        """ Updates or deletes an existing catalog entry.

        @param request: the HTTP request received by the server
        @param id: the id of the catalog entry
        """

        form = CatalogEntryForm(request.POST)
        if form.is_valid():
            entry = get_object_or_404(CatalogEntry, id=id)

            if request.POST.get('action') == 'Update':
                # update the existing catalog entry
                entry.name = form.cleaned_data.get('name')
                entry.description = form.cleaned_data.get('description')
                entry.save()

                messages.success(request, 'Item updated successfully')
                return redirect('inventory:catalog-entry', id)

            elif request.POST.get('action') == 'Delete':
                # delete the existing catalog entry
                try:
                    entry.delete()
                    messages.success(
                        request,
                        'Item successfully deleted from catalog'
                    )
                    return redirect('inventory:index')
                except models.ProtectedError:
                    # if fail to delete, give error message and redirect to same page
                    messages.error(
                        request,
                        'Cannot delete item from catalogue: Item exists in shipment'
                    )
                    return redirect('inventory:catalog-entry', id)

            else:
                return redirect('inventory:catalog-entry', id)

        else:
            return redirect('inventory:catalog-entry', id)


class AddInventoryItemView(View):
    def get(self, request):
        """ Displays form for creating a new inventory item.

        @param request: the HTTP request received by the server
        """

        context = {
            'form': InventoryItemForm()
        }
        return render(request, 'inventory/add-inventory-item.html', context)

    def post(self, request):
        """ Creates a new inventory item.

        @param request: the HTTP request received by the server
        """

        form = InventoryItemForm(request.POST)
        if form.is_valid():
            InventoryItem.objects.create(
                entry=form.cleaned_data.get('entry'),
                date=form.cleaned_data.get('date'),
                quantity=form.cleaned_data.get('quantity'),
            )
            return redirect('inventory:index')

        else:
            return redirect('inventory:add-item')


class InventoryItemView(View):
    def get(self, request, id):
        """ Displays single inventory item with the option to edit or delete the item.

        @param request: the HTTP request received by the server
        @param id: the id of the inventory item
        """

        # get inventory item and prepopulate form fields with inventory item
        shipment = get_object_or_404(InventoryItem, id=id)
        context = {
            'item': shipment,
            'form': InventoryItemForm(instance=shipment)
        }
        return render(request, 'inventory/inventory-item.html', context)

    def post(self, request, id):
        """ Updates or deletes an existing inventory item.

        @param request: the HTTP request received by the server
        @param id: the id of the inventory item
        """

        form = InventoryItemForm(request.POST)
        if form.is_valid():
            item = get_object_or_404(InventoryItem, id=id)

            if request.POST.get('action') == 'Update':
                # update the existing inventory item
                item.entry = form.cleaned_data.get('entry')
                item.date = form.cleaned_data.get('date')
                item.quantity = form.cleaned_data.get('quantity')
                item.save()

                messages.success(
                    request,
                    'Inventory item updated successfully'
                )
                return redirect('inventory:item', id)

            elif request.POST.get('action') == 'Delete':
                # delete the existing inventory item
                item.delete()
                messages.success(
                    request,
                    'Inventory item deleted successfully'
                )
                return redirect('inventory:index')

            else:
                # unknown request
                return redirect('inventory:item', id)

        else:
            return redirect('inventory:item', id)
