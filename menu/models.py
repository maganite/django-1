from django.db import models

# item
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField()

    # category

# category
# name
