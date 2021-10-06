from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices

# Create your models here.

class House(models.Model):
    title = models.CharField(max_length=25, default="House")
    location = models.CharField(max_length=40)
    price = models.IntegerField()
    rooms = models.CharField(max_length=10, default="Undefined")
    parking = models.CharField(max_length=10, default="Undefined")
    # TYPE = Choices(('Rent', 'Sale'),)
    type = models.CharField(max_length=10)
    # type = models.CharField(choices=TYPE, default="Rent", max_length=10)

    @property
    def price_display(self):
        return "KES%s" % self.price

    class Meta:
        verbose_name = 'House'
        verbose_name_plural = 'Houses'

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.house)
