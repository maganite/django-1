from django.shortcuts import render

# Create your views here.

def booking(request):
    return render(request,'booking.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')