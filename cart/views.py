from django.shortcuts import render , redirect
from Products.models import *
from .models import *
# Create your views here.

def orders_detail(request) :
    orders = Cart.objects.filter(user_id=request.user.id)
    return render(request , 'Cart/orders_show.html' , {'orders' : orders})
def add_order(request , id_product):
    url = request.META.get('HTTP_REFERER')
    data = Cart.objects.filter(product_id=id_product , user_id=request.user.id)
    if data :
        check = 'Yes'
    else :
        check = 'No'
    if request.method == 'POST' :
        form = CartForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data['quantity']
            if check == 'Yes' :
                order = Cart.objects.get(product_id=id_product , user_id=request.user.id)
                order.quantity += info
                order.save()
            if check == 'No' :
                Cart.objects.create(product_id=id_product , user_id=request.user.id , quantity=info)
        return redirect(url)

def remove_order(request , id_product) :
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id_product).delete()
    return redirect(url)

