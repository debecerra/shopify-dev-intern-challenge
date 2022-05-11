from django import forms
from .models import CatalogEntry, InventoryItem

# Django Documentation, Creating Forms from Models, https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#creating-forms-from-models


class CatalogEntryForm(forms.ModelForm):
    class Meta:
        model = CatalogEntry
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['entry', 'date', 'quantity']
        widgets = {
            'entry': forms.Select(attrs={'class': 'form-control'}),
            # djvg, https://stackoverflow.com/users/4720018/djvg, 
            # How to use a DatePicker in a ModelForm in django?, https://stackoverflow.com/a/69108038
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
