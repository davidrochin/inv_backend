from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_lenght=100)
    price = models.DecimalField(decimal_places=2)
    category_id = models.PositiveIntegerField()
    provider_id = models.PositiveIntegerField()