from django.contrib.auth.models import User, Group
from rest_framework import serializers
from inventory.models import Item, Document, Movement, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'code', 'price', 'category_id', 'provider_id')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'date')

class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ('id', 'document_id', 'item_id', 'quantity_in')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'color')