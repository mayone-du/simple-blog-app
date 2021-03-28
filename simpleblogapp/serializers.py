from rest_framework import serializers
from .models import PostModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ("id", "username", "password")
    extra_kwargs = {"password": {"write_only": True, "required": True}}

  def create(self, validated_date):
    user = User.objects.create_user(**validated_date)
    return user


class PostSerializer(serializers.ModelSerializer):

  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
  class Meta:
    model = PostModel
    fields = ("id", "title", "contents", "created_at", "updated_at")