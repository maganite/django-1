from django.db import models

# item
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #style = models.CharField(max_length=60)
    #number = models.IntegerField()
    # category

# category
# name

class category(models.Model):
    choice=[
        ("br","breakfast"),
        ("lu","lunch"),
        ("sn","snacks"),
        ("dn","dinner")
    ]
    name = models.CharField(max_length=120)#name of dish
    category = models.CharField(max_length=2,choices=choice)
