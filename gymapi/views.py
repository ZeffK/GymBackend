from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import customerSerializer,UserSerializer
from .models import customer,User

from rest_framework.views import APIView
from rest_framework.response import Response



# class customerViewSet(viewsets.ModelViewSet):
#     queryset=customer.objects.all().order_by('name')
#     serializer_class=customerSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all().order_by('name')
#     serializer_class=UserSerializer



class UserList(APIView):

    def get(self,req):
        user = User.objects.all()
        serial = UserSerializer(user,many=True)
        return Response(serial.data)
    def post(self,req):
        user = req.data.get('user')
        # Create an article from the above data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(article_saved.email)})

class customerList(APIView):

    def get(self,req):
        Customer = customer.objects.all()
        serial = customerSerializer(Customer,many=True)
        return Response(serial.data)
    
    def post(self,req):

        return Response("User Created")
        