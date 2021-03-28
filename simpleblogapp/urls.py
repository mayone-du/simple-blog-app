from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import PostListView, PostRetrieveView, PostSetView, CreateUserView


router = routers.DefaultRouter()
router.register("posts", PostSetView, basename="posts")

urlpatterns = [
  path("post-list/", PostListView.as_view(), name="post-list"),
  path("post-detail/<int:pk>/", PostRetrieveView.as_view(), name="post-detail"),
  path("register/", CreateUserView.as_view(), name="register"),
  path("auth/", include("djoser.urls.jwt")),
  path("", include(router.urls)),
]