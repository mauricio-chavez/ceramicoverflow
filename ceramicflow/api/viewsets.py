from forum.models import Post, Comments
from supplier.models import Suppliers, Reviews

from .serializers import PostSerializer, CommentsSerializer, ReviewsSerializer, SuppliersSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostList(APIView):

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsView(APIView):

    def get(self, request, format=None):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuppliersView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        suppliers = Suppliers.objects.all()
        serializer = SuppliersSerializer(suppliers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewsView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)