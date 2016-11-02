from __future__ import unicode_literals
from django.db import models
from details.models import Item

class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True)
	product = models.ForeignKey(Item)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title


class Cart(models.Model):
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return "Cart id: %s" %(self.id)
