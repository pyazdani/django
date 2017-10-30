# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages

def index(request):
    return render(request, "main_app/index.html")

def new_user(request):
    user = User.userManager.register(
        request.POST['name'],
        request.POST['username'],
        request.POST['password'],
        request.POST['confirm'],
    )
    if user[0]:
        request.session["user"] = {
            "id": user[1].id,
            "name": user[1].name
        }
        return redirect('/quotes')
    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')

def new_session(request):
    valid = User.userManager.login(
        request.POST['username'],
        request.POST['password']
    )
    if valid[0]:
        request.session["user"] = {
            "id": valid[1].id,
            "name": valid[1].name
        }
        return redirect('/quotes')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')

def quotes(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
    	user_id = request.session['user']['id']
        context = {
            'quotes': Quote.quoteManager.all(),
        }
        return render(request, 'main_app/quotes.html', context)

def add(request):
    if 'user' not in request.session:
        return redirect('/')
    elif request.method == 'POST':
    	user_id = request.session['user']['id']
    	quote = Quote.quoteManager.validate(request.POST, user_id)

        return redirect('/quotes')

def logout(request):
    request.session.clear()
    return redirect('/')