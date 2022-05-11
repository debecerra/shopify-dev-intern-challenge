from django.db import models


class CatalogItem(models.Model):
    """ Represents an inventory item in a catalog.
    """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    """ Represents a time specific shipment of an inventory item.
    """

    item = models.ForeignKey(CatalogItem, on_delete=models.PROTECT)
    date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.date}: {self.item} - {self.quantity}'
