from django.urls import path
from .views import PostList, PostDetail, UserDetail, UserList

urlpatterns = [
    path('post', PostList.as_view()),
    path('post/detail/<int:pk>', PostDetail.as_view()),

    path('users', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]