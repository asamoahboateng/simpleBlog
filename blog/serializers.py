from cgitb import lookup
from pyexpat import model
from rest_framework import serializers

from .models import Post, Comment

post_detail_url = serializers.HyperlinkedIdentityField(
    view_name = 'detail',
        # lookup_field = 'id'
)

class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'comment_detail', 
        # lookup_field = 'id'
    )
    # post = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='detail'
    # )
    class Meta:
        model = Comment
        fields = [
            'id',
            'url',
            'body',
            'post',
            # 'post'
        ]
        
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
    # comments = serializers.PrimaryKeyRelatedField(
    #     many =True,
    #     read_only = True
    # )
    comments = CommentSerializer(many=True, read_only=True)
    # comments = serializers.StringRelatedField(many=True)
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
        ]

