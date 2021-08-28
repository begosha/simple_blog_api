from rest_framework import generics
from posts.models import Post
from posts.serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostUpvoteSerializer
)


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer


class PostUpvoteView(generics.CreateAPIView):
    serializer_class = PostUpvoteSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

