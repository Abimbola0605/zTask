from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from .models import link
from .serializer import LinkSerializer
# Create your views here.

class PostListApi(ListAPIView):
    queryst = link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostCreateApi(CreateAPIView):
    queryst = link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(RetrieveAPIView):
    queryst = link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateApi(UpdateAPIView):
    queryst = link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDeleteApi(DestroyAPIView):
    queryst = link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
