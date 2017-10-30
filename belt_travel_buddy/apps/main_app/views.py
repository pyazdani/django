# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Trip
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
        return redirect('/travels')
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
        return redirect('/travels')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')

def travels(request):
    if 'user' not in request.session:
        return redirect('/')
    else: 
        context = {
            'trips': User.userManager.get(id=request.session['user']['id']).trips.all(),
            'all_trips': Trip.tripManager.exclude(users=request.session['user']['id']),
        }
        return render(request, "main_app/travels.html", context)

def add(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return render(request, 'main_app/add.html')



def process(request):

    if 'user' not in request.session:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'main_app/add.html')

    elif request.method == 'POST':
        trip = Trip.tripManager.validate(
            request.POST['destination'],
            request.POST['description'],
            request.POST['start_date'],
            request.POST['end_date'],
            )
        if trip[0]:
            u = User.userManager.get(id=request.session['user']['id'])
            u.save()
            trip[1].users.add(u)
            trip[1].save()
            return redirect('/travels')

        else:
            for error in trip[1]:
                messages.add_message(request, messages.ERROR, error)
    return redirect('/travels/add')

    # elif request.method == 'POST':
    #     trip = Trip.tripManager.validate(
    #         request.POST['destination'],
    #         request.POST['description'],
    #         request.POST['start_date'],
    #         request.POST['end_date'],
    #         )   
    #     u = User.userManager.get(id=request.session['user']['id'])
    #     u.save()
    #     trip[1].users.add(u)
    #     trip[1].save()
    #     return redirect('/travels')


def logout(request):
    request.session.clear()
    return redirect('/')

def destination(request, id):
    if 'user' not in request.session:
        return redirect('/')

    else:
        trip = Trip.tripManager.get(id=id)
        all_users = trip.users.all()
        context = {
            'destination': trip.destination,
            'description': trip.description,
            'start_date': trip.start_date,
            'end_date': trip.end_date,
            'planner': trip.users.first(),
            'all_users': trip.users.all(),
        }
        return render(request, 'main_app/destination.html', context)

def join(request, id):
    u = User.userManager.get(id=request.session['user']['id'])
    u.save()
    trip = Trip.tripManager.get(id=id)
    trip.users.add(u)
    trip.save()
    return redirect('/travels')

def leave(request, id):
    u = User.userManager.get(id=request.session['user']['id'])
    u.save()
    trip = Trip.tripManager.get(id=id)
    u.trips.remove(trip)
    u.save()
    return redirect('/travels')