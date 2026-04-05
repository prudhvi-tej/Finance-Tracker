from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Transaction
from .serializers import TransactionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import RolePermission
from rest_framework.filters import SearchFilter

class TransactionViewset(ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    permission_classes=[RolePermission]

    filter_backends=[DjangoFilterBackend]
    filterset_fields=['type','category','date']
    search_fields = ['category', 'description']
    


