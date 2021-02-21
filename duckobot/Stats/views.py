from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

# Create your views here.

def home_view(request, *args, **kwargs): # *args, **kwargs

    return render(request, "index.html", {}) # string of HTML code