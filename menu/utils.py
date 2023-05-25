from menu.models import *


def printItem():
    print(Item.objects.all())