from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from personal_blog.models import Blog

from .permissions import IsAuthorOrReadOnly
from .serializers import BlogSerializer


class APIBlogList(APIView):
    permission_classes = [IsAuthorOrReadOnly]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIBlogDetail(APIView):
    permission_classes = [IsAuthorOrReadOnly]

    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            self.check_object_permissions(request, blog)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, blog)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            self.check_object_permissions(request, blog)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            self.check_object_permissions(request, blog)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
