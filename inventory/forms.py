from django import forms
from .models import CatalogItem, Shipment

# Django Documentation, Creating Forms from Models, https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#creating-forms-from-models


class CatalogItemForm(forms.ModelForm):
    class Meta:
        model = CatalogItem
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['item', 'date', 'quantity']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            # djvg, How to use a DatePicker in a ModelForm in django?, https://stackoverflow.com/a/69108038
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
