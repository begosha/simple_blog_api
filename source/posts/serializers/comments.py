from rest_framework import serializers
from posts.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = (
            'content',
            'author',
            'post',
        )
        model = Comment

    def to_representation(self, instance):
        return instance.content


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = (
            'author',
            'content',
            'post',
        )
        model = Comment

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        Comment.objects.create(
            content=validated_data['content'],
            author=user,
            post=validated_data['post']
        )
        return validated_data
