from django.db import models

# Create your models here.
from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField


CATEGORY = (
    ('S', 'Small Plants'),
    ('M', 'Medium Plants'),
    ('B', 'Big Plants'),
    ('A', 'Accessories')
)


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        """ This function will return url from product"""

        return reverse("store:product-detail", kwargs={
            "pk": self.pk
        })

    def get_add_to_cart_url(self):
        """ This function will  return url to function add
         item to cart in views.py file """

        return reverse("store:add-to-cart", kwargs={
            "pk": self.pk
        })

    def get_remove_from_cart_url(self):
        """will return url to function remove item from cart in views.py file """

        return reverse("store:remove-from-cart", kwargs={
            "pk":self.pk
        })



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    stripe_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username




class Carousel(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=150, blank=True, default="")
    subtext_1 = models.TextField(blank=True, default="")
    subtext_2 = models.TextField(blank=True, default="")
    subtext_3 = models.TextField(blank=True, default="")


    def __str__(self):
        return self.title