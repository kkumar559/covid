from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'covid/index.html')

def about(request):
    return render(request,'covid/about.html')
