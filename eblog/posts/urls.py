from django.urls import path, include
from rest_framework import routers

from . import views
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', include(router.urls)),
]