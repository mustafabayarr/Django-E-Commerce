from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def amount(self):
        return self.quantity*self.product.price

    @property
    def price(self):
        return  self.product.price

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']