from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.utils import timezone
from .models import Post


def start_window(request):
    return render(request, 'home.html')


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
