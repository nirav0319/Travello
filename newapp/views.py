from django.shortcuts import render
from django.http import HttpResponse
from .models import destination
# Create your views here.
def index(request):
    des=destination.objects.all()
    return render(request,'index.html',{'des':des})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def destinations(request):
    return render(request,'destinations.html')
def elements(request):
    return render(request,'elements.html')
def news(request):
    return render(request,'news.html')
