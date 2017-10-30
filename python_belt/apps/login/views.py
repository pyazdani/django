from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, UserManager
import bcrypt

def index(request):
    return render(request, 'login/index.html')

def register(request):
    user = User.userManager.register(request.POST['name'], request.POST['alias'], request.POST['email'], request.POST["password"], request.POST["confirm_password"], request.POST['dob'])
    if user[0]:
        request.session['user_id'] = user[1].id
        request.session['email'] = user[1].email
        request.session['name'] = user[1].name
        request.session['alias'] = user[1].alias
        return redirect('/quotes')
    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def login(request):
    user = User.userManager.login(request.POST['email'], request.POST["password"])
    if user[0]:
        request.session['user_id'] = user[1].id
        request.session['email'] = user[1].email
        return redirect('/quotes')
    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')