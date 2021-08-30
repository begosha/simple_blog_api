from django.urls import path
from posts.views import (
    posts,
    comments,
    users
)
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Blog API')
urlpatterns = [
    url(r'^$', schema_view),
    path('post/', posts.PostList.as_view()),
    path('post/create/', posts.PostCreateView.as_view()),
    path('upvote/', posts.PostUpvoteView.as_view()),
    path('<int:pk>/post', posts.PostDetail.as_view()),
    path('comment/', comments.CommentList.as_view()),
    path('comment/create', comments.CommentCreateView.as_view()),
    path('<int:pk>/comment', comments.CommentDetail.as_view()),
    path('users/', users.UserList.as_view()),
    path('users/<int:pk>/', users.UserDetail.as_view()),
]