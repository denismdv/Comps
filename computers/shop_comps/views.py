from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import *
from .models import Computers
from .serializers import CompsSerializer


class CompsViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all().order_by('-price')
    serializer_class = CompsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['chipset', 'ram', 'price']


