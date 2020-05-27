from rest_framework import serializers
from .models import customer,User

class customerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=customer
        fields=('name','address','email','mobile')

        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model=User
        fields=('name','email','password')
