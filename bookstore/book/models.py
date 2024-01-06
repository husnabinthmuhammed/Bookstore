from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=250)
    description = models.TextField(default=True, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    image_url = models.CharField(max_length=2083, blank=True, default=False)
    book_available = models.BooleanField(default=False)

    #def __str__(self):
    #    return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Books)
    total_price = models.DecimalField(max_digits=10, decimal_places=5)

class CartItems(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    #def total_price(self):
    #    return self.books.price * self.quantity
