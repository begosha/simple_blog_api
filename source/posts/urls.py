from django.urls import path
from posts.views import (
    posts,
    comments,
    users
)

urlpatterns = [
    path('', posts.PostList.as_view()),
    path('create/', posts.PostCreateView.as_view()),
    path('upvote/', posts.PostUpvoteView.as_view()),
    path('<int:pk>/post', posts.PostDetail.as_view()),
    path('comments/', comments.CommentList.as_view()),
    path('comment/create', comments.CommentCreateView.as_view()),
    path('<int:pk>/comment', comments.CommentDetail.as_view()),
    path('users/', users.UserList.as_view()),
    path('users/<int:pk>/', users.UserDetail.as_view()),
]