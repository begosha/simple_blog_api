from rest_framework import serializers
from posts.models import Post, Upvote


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'author',
            'upvote_number',
            'created_at',
            'comments'
        )
        model = Post


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'author',
            'upvote_number',
        )
        model = Post

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        Post.objects.create(
            title=validated_data['title'],
            author=user,
            url=validated_data['url']
        )
        return validated_data


class PostUpvoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = (
            'author',
            'post',
        )
        model = Upvote

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        Upvote.objects.create(
            author=user,
            post=validated_data['post']
        )
        post = Post.objects.get(id=validated_data['post'].pk)
        post.upvote_number += 1
        post.save()
        return validated_data
