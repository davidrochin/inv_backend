import random
import json
import datetime

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group

from django_seed import Seed

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.serializers import UserSerializer, GroupSerializer, ItemSerializer, DocumentSerializer, MovementSerializer, CategorySerializer
from inventory.models import Item, Document, Movement, Category


def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")


def monthly_out(resquest, item_id):
    value = item_id

    # Calcular cuantos productos de cierto articulo salen en promedio mensualmente de inventario
    print(Movement.objects.filter(quantity_in__gt=0))

    return JsonResponse(value, safe=False)


def all_items(request):
    serializer = ItemSerializer(Item.objects.all(), many=True)

    return JsonResponse({'results': serializer.data}, safe=False)


def seed(request):
    seeder = Seed.seeder()

    # Las categorías iniciales
    cat = Category()
    cat.name = 'Alimentos'
    cat.color = 'ff695b'
    cat.save()

    cat = Category()
    cat.name = 'Bebidas'
    cat.color = '60a8ff'
    cat.save()

    print('Seeded categories')

    seeder.add_entity(Item, 10, {
        'name': lambda x: seeder.faker.word() + ' ' + seeder.faker.word(),
        'code': lambda x: None,
        'provider_id': lambda x: None,
        'lead_time': lambda x: None,
        'reorder_point': lambda x: None,
        'price': lambda x: random.randint(10, 500),
        'category_id': lambda x: Category.objects.order_by('?').first(),
    })

    seeder.execute()
    print('Seeded items')

    # Crear 20 documentos para cada mes del año
    for i in range(0, 12):
        seeder.add_entity(Document, 20, {
            'date': lambda x: datetime.date(2019, random.randint(1, 12), random.randint(1, 28)),
        })

    seeder.execute()
    print('Seeded documents')

    # Crear 5 movimientos para cada documento
    for doc in Document.objects.all():
        print(doc.id)
        # seeder.add_entity(Movement, 5, {
        #     'document_id': lambda x: doc,
        #     'item_id': lambda x: Item.objects.order_by('?').first(),
        #     'quantity_in': lambda x: random.randint(-5, 5),
        # })

        for i in range(0, 5):
            mov = Movement()
            mov.document_id = doc
            mov.item_id = Item.objects.order_by('?').first()
            mov.quantity_in = random.randint(-5, 5)
            mov.save()

        #seeder.execute()

    print('Seeded movements')

    return HttpResponse("Seeded succesfully")


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

    # def get_queryset(self):
    # print(self.kwargs)
    ##    document_id = self.kwargs['document_id']
    # return Movement.objects.filter(document_id = document_id)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
