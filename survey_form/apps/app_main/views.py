from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
	if not 'counter' in request.session:
		request.session['counter'] = 0
	return render(request, "app_main/index.html")

def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['message'] = request.POST['message']
	return redirect("/result")

def result(request):
	request.session['counter'] += 1
	return render(request, "app_main/result.html")

def home(request):
	return redirect('/')
