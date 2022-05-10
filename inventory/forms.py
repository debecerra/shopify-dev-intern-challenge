from django import forms
from .models import Item, Shipment

# Django Documentation, Creating Forms from Models, https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#creating-forms-from-models


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
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
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
