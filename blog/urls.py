from django.urls import include, path
from blog.serializers import LikesSeralizer, UserSeralizer
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view(), name="detail"),
    path('comments', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name="comment_detail"),
    
    path('users', views.UserList.as_view(), name="user-list"),
    path('likes', views.LikesList.as_view(), name='likes-list'),
]