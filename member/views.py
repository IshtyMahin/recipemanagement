from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializers import UserSerializer
# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class =UserSerializer
    
    