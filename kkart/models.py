from django.db import models
from shop.models import Product


# Create your models here.

class Caart(models.Model):
    caart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Caart'
        ordering = ['date_added']

    def __str__(self):
        return self.caart_id


class CaartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    caart = models.ForeignKey(Caart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    activity = models.BooleanField(default=True)

    class Meta:
        db_table = 'CaartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
