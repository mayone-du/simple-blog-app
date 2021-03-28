from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, PostSerializer
from .models import PostModel

# Create your views here.

class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = (AllowAny,)

class PostListView(generics.ListAPIView):
  queryset = PostModel.objects.all()
  serializer_class = PostSerializer
  permission_classes = (AllowAny,)

class PostRetrieveView(generics.RetrieveAPIView):
  queryset = PostModel.objects.all()
  serializer_class = PostSerializer
  permission_classes = (AllowAny,)


class PostSetView(viewsets.ModelViewSet):
  queryset = PostModel.objects.all()
  serializer_class = PostSerializer
