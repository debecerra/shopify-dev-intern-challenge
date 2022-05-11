from django.db import models


class CatalogEntry(models.Model):
    """ Represents an inventory item in a catalog.
    """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    """ Represents specific instance of an inventory item.
    """

    entry = models.ForeignKey(CatalogEntry, on_delete=models.PROTECT)
    date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.date}: {self.entry} - {self.quantity}'
