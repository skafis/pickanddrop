
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from details.models import Item
from .models import Cart, CartItem
from shopping_cart.forms import PesapalForm
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

def view_cart(request):
	ctx = {}
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
		ctx['cart'] = cart
		ctx['pk'] = int(cart.total)
	except:
		ctx['empty'] = True
		ctx['empty_message'] = "Your Cart is Empty, please keep shopping."

	return render(request, "shopping_cart/view_cart.html", ctx)

# def checkout(request,amount):
# 	ctx = {}
# 	form = PesapalForm(request.POST or None)
# 	form.fields['amount'].initial = amount
# 	ctx['form'] = form
# 	ctx['amount'] = amount
# 	the_id = request.session['cart_id']

# 	if request.method == 'POST':
# 		try:
# 			the_id = request.session['cart_id']
# 			cart = Cart.objects.get(id=the_id)
# 			description ="Payment for %s"%(cart)
# 			amount = request.POST['amount']
# 			first_name = request.POST['first_name']
# 			last_name = request.POST['last_name']
# 			email = request.POST['email']
# 			types="MERCHANT"
# 			reference="001"

# 			#to save the data to the repots
# 			p = PesapalPayment.objects.create(cart = cart, description= description, amount = amount, 
# 				first_name = first_name, last_name= last_name, email = email, types = types, reference = reference)
# 			return redirect('http://192.168.0.13/ubrica_pesapal/pesapal-iframe.php?first_name=%s&last_name=%s&amount=%s&email=%s&description=%s&type=%s&reference=%s'%
# 					(first_name,last_name, amount, email,description,types,reference))
# 		except:
# 			raise
# 			ctx['empty'] = True
# 			ctx['empty_message'] = "Your Cart is Empty, please keep shopping."

# 	return render(request, "shopping_cart/checkout.html", ctx)


def update_cart(request, pk):
	request.session.set_expiry(1200)
	try:
		qty = request.GET.get('qty')
		update_qty = True
	except:
		qty = None
		update_qty = False
	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id
	
	cart = Cart.objects.get(id=the_id)

	try:
		product = Item.objects.get(pk=pk)
	except Item.DoesNotExist:
		pass
	except:
		pass

	cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
	if created:
		print "yeah"

	if update_qty and qty:
		if int(qty) <= 0:
			cart_item.delete()
		else:
			cart_item.quantity = qty
			cart_item.save()
	else:
		pass
	new_total = 0.00
	for item in cart.cartitem_set.all():
		line_total = float(item.product.cost) * item.quantity
		new_total += line_total

	request.session['items_total'] = cart.cartitem_set.count()
	cart.total = new_total
	cart.save()
	return HttpResponseRedirect(reverse("shopping_cart:view_cart"))