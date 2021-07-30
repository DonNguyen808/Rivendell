from django.shortcuts import render
from . import models
from .models import Nursery

# Create your views here.
def home(request):
    nurseries = models.Nursery.objects.all()
    nurseries_dict = {
        'nurseries': nurseries
    }
    return render(request, 'base.html', nurseries_dict)

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html', working)




def new_search(request):
    return render(request, 'new_search.html')

def contact(request):
    return render(request, 'contact.html')

def new_search(request):
    # get returns a dictionary no the same as post/get python get
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'new_search', stuff_for_frontend)

