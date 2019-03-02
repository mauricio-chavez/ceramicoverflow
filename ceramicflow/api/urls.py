from django.urls import path
from . import viewsets
urlpatterns = [
    path('forum/post/', viewsets.PostList.as_view(), name='forum-post'),
    path('forum/comments/', viewsets.CommentsView.as_view(), name='forum-comment'),
    path('supplier/', viewsets.SuppliersView.as_view(), name='supplier'),
    path('supplier/review/', viewsets.ReviewsView.as_view(), name='supplier-review'),
]