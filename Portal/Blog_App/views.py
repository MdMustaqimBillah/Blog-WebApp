from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    dictionary = {
        
    }
    return render(request, 'Blog_App/index.html', context=dictionary)
