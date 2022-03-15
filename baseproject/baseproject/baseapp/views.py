from django.http import HttpResponse
from django.shortcuts import render
from . models import food

# Create your views here.

def demo(request):
    obj = food.objects.all()
    return render(request,'index.html',{'result':obj})
