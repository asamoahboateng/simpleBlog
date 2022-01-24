from django.http import QueryDict
from rest_framework import generics
from .serializers import CommentSerializer, LikesSeralizer, PostDetailSeralizer, PostListSerializer, UserSeralizer
from .models import Likes, Post, Comment, User


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
    
class LikesList(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSeralizer
    
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_clas = UserSeralizer