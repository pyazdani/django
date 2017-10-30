# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(req):
	return render(req, "first_app/index.html")

def home(req):
	return render(req, "first_app/home.html", {"name" : "passing a variable "})
