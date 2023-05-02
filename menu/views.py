from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')