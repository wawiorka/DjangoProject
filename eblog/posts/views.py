from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from django.views.decorators.csrf import requires_csrf_token


def start_window(request):
    return render(request, 'home.html')


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
