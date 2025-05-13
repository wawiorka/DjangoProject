from django.contrib import admin
from .models import Post
from users.models import User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author_id", "created_at", "published_at")

