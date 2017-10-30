# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(req):
	return render(req, "blogs/index.html")

def new(req):
	return render(req, "blogs/new.html", {"name" : "passing a variable "})

def create(req):
	return redirect('/')

def show(req, blog_id):
    print blog_id
    return render("blogs/{}".format(blog_id))

def edit(req, blog_id):
    return render("blogs/{}".format(blog_id))
    
def destroy(request, blog_id):
    return redirect('/')

# ##Alternative method using HttpResponse rather than render##

# def index(request):
#     return HttpResponse("placeholder to later display all the list of blogs")

# def new(request):
#     return HttpResponse("placeholder to display a new form to create a new blog")
    
# def create(request):
#     return redirect('/')

# def show(request, blog_id):
#     print blog_id
#     return HttpResponse("placeholder to display blog {}".format(blog_id))

# def edit(request, blog_id):
#     return HttpResponse("placeholder to edit blog {}".format(blog_id))
    
# def delete(request, blog_id):
#     return redirect('/')
