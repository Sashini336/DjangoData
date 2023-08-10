from django.shortcuts import render
from rest_framework import generics
from .models import Ads
from rest_framework  import viewsets
from django.contrib import admin
from django.contrib.auth.models import User
from Ads.serializers import AdsSerializer, UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer  
    
    