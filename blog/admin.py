from django.contrib import admin
from .models import Post, Comment, Likes, User
import datetime
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(User)