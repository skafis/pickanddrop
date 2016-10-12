from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.
class Userdetails(models.Model):
	first_name = models.CharField(max_length= 100)
	slug = models.SlugField(unique=True)
	last_name = models.CharField(max_length= 100)
	email = models.EmailField()
	telephone = models.CharField(max_length=15)
	country = models.CharField(max_length=250)
	amount = models.DecimalField(max_digits=20, decimal_places=2)
	

	def __str__(self):
		return self.first_name

	def get_absolute_url(self):
		return reverse("location", kwargs={'slug': self.slug})

def create_slug(instance,new_slug = None):
    slug = slugify(instance.first_name)
    if new_slug is not None:
        slug = new_slug
    qs = Userdetails.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_receiver, sender=Userdetails)


class Delivery(models.Model):
	# user = models.ForeignKey(Userdetails, null=False)
	first_name = models.CharField(max_length= 100)
	last_name = models.CharField(max_length= 100)
	email = models.EmailField()
	amount = models.CharField(max_length=20)

	def get_absolute_url(self):
		return reverse('location', kwargs={'slug': self.slug})

class Merchant(models.Model):
	company = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField()
	telephone = models.CharField(max_length=15)
	location = models.CharField(max_length=40)

	def __str__(self):
		return self.company

	def get_absolute_url(self):
		return reverse('info', kwargs={'slug': self.slug})

class Item(models.Model):
	name = models.ForeignKey(Merchant, verbose_name = 'Name', blank = True)
	item_name = models.CharField(max_length=40)
	cost = models.DecimalField(max_digits=20, decimal_places=2)
	






