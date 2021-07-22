from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Post
from .serializers import PostSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
def post_list(request, category_name):
    posts = Post.objects.filter(category__name=category_name)
    if request.method == 'GET':
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, category_name, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
