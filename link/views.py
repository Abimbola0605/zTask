from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DetailAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DeleteAPIView
from .models import link
# Create your views here.

class PostListApi(ListAPIView):
    queryst = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
class PostCreateApi(CreateAPIView):
    queryst = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(RetrieveAPIView):
    queryst = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateApi(UpdateAPIView):
    queryst = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDeleteApi(DestroyAPIView):
    queryst = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
