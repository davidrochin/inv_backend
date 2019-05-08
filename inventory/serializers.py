from django.contrib.auth.models import User, Group
from rest_framework import serializers
from inventory.models import Item, Document, Movement

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url', 'name', 'code', 'price', 'category_id', 'provider_id')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ('url', 'date')

class MovementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movement
        fields = ('url', 'document_id', 'item_id', 'quantity_in')