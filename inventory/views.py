from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics

from inventory.serializers import UserSerializer, GroupSerializer, ItemSerializer, DocumentSerializer, MovementSerializer, CategorySerializer
from inventory.models import Item, Document, Movement, Category

def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    filter_fields = {'document_id'}

    ##def get_queryset(self):
    ##    print(self.kwargs)
    ##    document_id = self.kwargs['document_id']
    ##    return Movement.objects.filter(document_id = document_id)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer