from celery import task
from celery.utils.log import get_task_logger
from posts.models import Post

logger = get_task_logger(__name__)


@task
def task_reset_upvotes():
    for post in Post.objects.all():
        post.upvote_number = 0
        post.save()
    logger.info("Upvotes are reset")
