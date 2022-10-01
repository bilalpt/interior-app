from django.shortcuts import render
from django.http import HttpResponse

from .models import products

# Create your views here.
 

def app(request):
    return render(request,'home.html')
def app1(request):
    dict_prod={
        'shop' : products.objects.all()
    }
    return render(request,'product.html',dict_prod)
def app2(request):
    return render(request,'contact.html')
def app3(request):
    return render(request,'about.html')

def app4(request):
    return render(request,'new.html')    

        