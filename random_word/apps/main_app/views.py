from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	unique_id = get_random_string(length=14)

	request.session['random'] = unique_id

	if not 'counter' in request.session:
		request.session['counter'] = 1

	return render(request, "main_app/index.html")

def random_word(request):
	unique_id = get_random_string(length=14)

	request.session['random'] = unique_id
	request.session['counter'] += 1
	return redirect ('/')

def reset(request):
	request.session.clear()
	return redirect('/')
