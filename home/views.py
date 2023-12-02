from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    context = {
        'book': Book.objects.all(),
        'turi': Turi.objects.all(),
        'autor': Autor.objects.all(),
    }
    return render(request, 'index.html',context)