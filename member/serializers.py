from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Member 
        fields = '__all__'
        
