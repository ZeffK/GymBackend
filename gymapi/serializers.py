from rest_framework import serializers
from .models import customer,User
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from rest_framework.serializers import CharField,EmailField,ValidationError
from django.contrib.contenttypes.models import ContentType
salt="VerySecret"
class customerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=customer
        fields=('name','address','email','mobile')

        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model=User
        fields=('name','email','password')
    
    def create(self, validated_data):
        user = User.objects.create(
            name =validated_data['name'],
            email= validated_data['email'],
            password = make_password(validated_data['password'],salt=salt)
        )
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    user_obj=None
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)
    class Meta:
        model = User
        fields=['email','password','token']

    def validate(self,data):
        question=data.get("email",None)
        passs= data.get("password",None)
        if not question:
            raise ValidationError("Email is required")

        user = User.objects.filter(
            Q(email=question)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This Email is not Valid")
        if user_obj:
            if not check_password(passs,user_obj.password):
                raise ValidationError("Incorrect Username/Password Combination")

        data['token']= "TOKEN"
        return data

 #data == Front end values
 #user_obj == data fetched from DB

        
# User.objects.data.email == email
# SELECT USER FROM USERTABLE WHERE EMAIL == SENTEMAIL