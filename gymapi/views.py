from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import customerSerializer,UserSerializer
from .models import customer,User



class customerViewSet(viewsets.ModelViewSet):
    queryset=customer.objects.all().order_by('name')
    serializer_class=customerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('name')
    serializer_class=UserSerializer