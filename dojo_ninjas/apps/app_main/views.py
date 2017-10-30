from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
	if not 'words' in request.session:  #<---Defines a "words" within session if one
		request.session['words'] = []	#<--- doesn't exit(won't override with if statement)

	return render(request, "app_main/index.html")

def create(request):
	if len(request.POST['word']) < 1:
		word = "default"
	else:
		word = request.POST['word']

	if not 'color' in request.POST:
		color = 'black'
	else:
		color = request.POST['color']

	if not 'font' in request.POST:
		font = 'off'
	else:
		font = request.POST['font']

	createdAt = datetime.now()
	createdAt = createdAt.strftime("%Y-%m-%d %H:%M %p")

	data = {
		'word': word,
		'color': color,
		'font' : font,
		'createdAt' : createdAt
	}

	words = request.session["words"] # <---List
	words.append(data) #<----appends data dictionary into the words list
	request.session["words"] = words #<---Sets r.w.words into the new appended words

	return redirect("/")

def clear(request):
	request.session.clear()
	return redirect("/")
