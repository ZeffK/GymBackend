from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import customerSerializer,UserSerializer,UserLoginSerializer
from .models import customer,User
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import ( AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
salt = "VerySecret"

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

class LoginUser(APIView):
    permission_classes= [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self,request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return Response(new_data,status=HTTP_200_OK)
        return Response(serializers.error,status=HTTP_400_BAD_REQUEST)
    