# from itsdangerous import serializer
from rest_framework import generics
from .serializers import CommentSerializer, PostDetailSeralizer, PostListSerializer
from .models import Post, Comment


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('date')
#     serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = PostListSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSeralizer
    
    
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer