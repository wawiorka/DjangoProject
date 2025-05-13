from django.contrib import admin
from .models import User
from posts.models import Post

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_joined")
    # list_display = ("username", "email", "date_joined", "show_summ_posts")


    # def show_summ_posts(self, obj):
    #     count = Post.objects.filter(id = Post.author_id).count()
    #     return count
    #
    # show_summ_posts.short_description = "Create posts"