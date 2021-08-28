from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Title'
    )
    url = models.URLField(
        blank=False,
        null=False,
        verbose_name='URL'
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=False,
        related_name='posts',
        verbose_name='Author'
    )
    upvote_number = models.PositiveIntegerField(
        null=False,
        blank=False,
        default=0,
        verbose_name='Upvote Number'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        verbose_name='Post',
        related_name='comments',
        blank=False,
        null=False
    )
    content = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Comment'
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=False,
        related_name='comments',
        verbose_name='Author'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content


class Upvote(models.Model):
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        verbose_name='Post',
        related_name='upvotes',
        blank=False,
        null=False
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=False,
        related_name='upvotes',
        verbose_name='Author'
    )

    class Meta:
        db_table = 'upvotes'
        verbose_name = 'Upvote'
        verbose_name_plural = 'Upvotes'

