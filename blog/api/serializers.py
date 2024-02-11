from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from personal_blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Blog
        exclude = ('id',)
