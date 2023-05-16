from django.shortcuts import render

from .models import Item

def menu(request):
    # menu_items = [
    #     {
    #         "name": "Dragon Chicken",
    #         "price": 300
    #     },
    #     {
    #         "name": "Fire Chinken",
    #         "price": 200
    #     }
    # ]
    menu_items = Item.objects.all()

    return render(request=request, template_name='menu.html', context={"menu": menu_items})

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')