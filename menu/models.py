from django.db import models

#CRUD = create read update delete operations
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #style = models.CharField(max_length=60)
    #number = models.IntegerField()
    # category
    #def __str__(self) -> str:
    #    return self.name



    