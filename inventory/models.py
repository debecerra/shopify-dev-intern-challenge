from django.db import models
from django.utils import timezone
import datetime

class CatalogEntry(models.Model):
    """ Represents an inventory item in a catalog.
    """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.name} (C{self.id})'


class Country(models.Model):
    """ Represents a country in the world.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    """ Represents a city in the world.
    """

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    temp = models.DecimalField(decimal_places=1, max_digits=4, default=0.0)
    weather = models.CharField(max_length=50, default="no weather info to display")
    date_modified = models.DateTimeField(auto_now=True)

    def outdated(self):
        threshold = timezone.now() - datetime.timedelta(minutes=5)
        return self.date_modified < threshold

    def __str__(self):
        return f'{self.name}, {self.country.name}'


class Warehouse(models.Model):
    """ Represents a warehouse that holds inventory items.
    """

    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city} (W{self.id})'


class InventoryItem(models.Model):
    """ Represents specific instance of an inventory item.
    """

    entry = models.ForeignKey(CatalogEntry, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.entry} - {self.quantity} @ {self.warehouse}'
