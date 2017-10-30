from __future__ import unicode_literals
from django.shortcuts import render, redirect
from products import items

def index(request):

    products = {
        "items" : items
    }

    if 'amount_charged' not in request.session:
        request.session['amount_charged'] = 0
        request.session['total_charged'] = 0
        request.session['total_items'] = 0
        request.session['quantity'] = 0

    charged = 0

    return render(request, "app_main/index.html", products)

def buy(request):

    for item in items:
        if item['id'] == request.POST['i_id']:
            request.session['total_charged'] = item['price'] * int(request.POST['quantity'])    

    request.session['total_items'] += int(request.POST['quantity'])
    request.session['quantity'] = request.POST['quantity']
    
    return redirect("/amadon/checkout")

def amadon_checkout(request):
    return render(request, "app_main/checkout.html")

