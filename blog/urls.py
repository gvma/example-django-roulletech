from django.urls import path
from .views import PostListCreate, CommentListCreate

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:post_id>/comments/', CommentListCreate.as_view(), name='comment-list-create')
]