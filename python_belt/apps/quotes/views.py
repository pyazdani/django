from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, UserManager, Quote, QuoteManager
from django.contrib import messages

def quotes(request):
    if 'user_id' not in request.session:
        messages.add_message(request, messages.ERROR, "You must first login")
        return redirect('/')
    context = {
        'quotes' : User.userManager.get(id=request.session['user_id']).quotes.all(),
        'all_quotes' : Quote.quoteManager.exclude(users = request.session['user_id'])
    }
    return render(request, 'quotes/quotes.html', context)

def add(request):
    quote = Quote.quoteManager.add(request.POST['author'], request.POST['message'], request.session['user_id'])
    if quote [0]:
        u = User.userManager.get(id=request.session['user_id'])
        u.save()
        quote = Quote.quoteManager.create(author=request.POST['author'], message=request.POST['message'])
        quote.save()
        quote.users.add(u)
        quote.save()
        return redirect('/quotes')
    else:
        for error in quote[1]:
            messages.add_message(request,messages.ERROR, error)
            return redirect('/quotes')

def library(request, user_id):
    user = User.userManager.get(id=request.session['user_id'])
    quote = Quote.quoteManager.get(id=quote_id)
    context = {
        'author' : quote.author,
        'message' : quote.message,
        'count' : '+=1',
        'font_color' : 'red',
    }
    return render(request, "quotes/library.html", context)

def fav(request, quote_id):
    quote = Quote.quoteManager.get(id=quote_id)
    liker = User.userManager.get(id=request.session['user_id'])
    liker.save()
    quote.users.add(liker)
    return redirect('/quotes')

def remove(request, quote_id):
    quote = Quote.quoteManager.get(id=quote_id)
    quote.save()
    quote.delete()
    return redirect('/quotes')