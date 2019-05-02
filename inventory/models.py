from django.db import models

class ItemManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)

class Item(models.Model):

    objects = ItemManager()

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    category_id = models.PositiveIntegerField(null=True)
    provider_id = models.PositiveIntegerField(null=True)

