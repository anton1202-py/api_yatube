from rest_framework import serializers

from posts.models import Group, Post, Comment


class PostSerializer (serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'image', 'group', 'pub_date', 'author')
        read_only_fields = ('author',)


class GroupSerializer (serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'created', 'author')
        read_only_fields = ('author', 'post')
