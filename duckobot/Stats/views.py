from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
import requests
# Create your views here.

def home_view(request, *args, **kwargs): # *args, **kwargs

    response = requests.get("https://ducktheduck.github.io/duckobot/data.json").json()
    
    context = {

        "name": response.get("name"),
        "tag": response.get("tag"),
        "guildSize": response.get("guildSize")

    }

    return render(request, "index.html", context) # string of HTML code