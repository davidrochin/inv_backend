from django.db import models
import datetime

class GenericManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name = name)

class Category(models.Model):

    objects = GenericManager()

    name = models.CharField(max_length=200)
    color = models.CharField(max_length=6, default='e52d2d')

class ItemManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)

class DocumentManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name = name)

class Item(models.Model):

    objects = ItemManager()

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    provider_id = models.PositiveIntegerField(null=True)

    reorder_point = models.DecimalField(decimal_places=2, max_digits=10, null = True)
    lead_time = models.DecimalField(decimal_places=2, max_digits=10, null = True)

class Document(models.Model):

    objects = DocumentManager()

    date = models.DateField(default = datetime.date.today)

class Movement(models.Model):

    objects = GenericManager()

    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_in = models.DecimalField(decimal_places=2, max_digits=10)


