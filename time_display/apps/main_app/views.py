from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render

def index(request):
    context = {
        "time": datetime.now()
    }
    return render(request, "main_app/index.html", context)