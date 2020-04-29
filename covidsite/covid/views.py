from django.shortcuts import render
from django.http import HttpResponse
from .models import Statelist

# Create your views here.
def faq1(request):
    return render(request,'covid/faq1.html')

def faq2(request):
    return render(request,'covid/faq2.html')

def faq3(request):
    return render(request,'covid/faq3.html')

def faq4(request):
    return render(request,'covid/faq4.html')


    
def index(request):
    all_elements = Statelist.objects.all
    return render(request,'covid/index.html',{'all':all_elements})

def about(request):
    return render(request,'covid/about.html')
