from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
