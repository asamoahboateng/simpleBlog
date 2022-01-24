from cgitb import lookup
from pyexpat import model
from rest_framework import serializers
from .models import Post, Comment, Likes, User

post_detail_url = serializers.HyperlinkedIdentityField(
    view_name = 'detail',
        # lookup_field = 'id'
)

class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'comment_detail',
    )
    class Meta:
        model = Comment
        fields = [
            'id',
            'url',
            'body',
            'post',
            # 'post'
        ]

class LikesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['likes','user','post']
        extra_kwargs = ('likes')

class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'user']
        
            
class PostListSerializer(serializers.ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = [
            'url',
            'pk',
            'title',
            # 'slug',
            'body',
            'created_at',
            'updated_at'
        ]
        extra_kwargs = {
            'slug' : {'required':False},
            'created_at' : {'required':False},
            'updated_at' : {'required':False},
        }

class PostDetailSeralizer(serializers.ModelSerializer):
    url = post_detail_url
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikesSeralizer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'pk',
            'title',
            'slug',
            'body',
            'created_at',
            'updated_at',
            'comments',
            'likes'
        ]


