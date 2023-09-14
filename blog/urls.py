from django.urls import path
from .views import list_posts, detail_post

urlpatterns = [
    path('', list_posts, name='list_posts'),
    path('posts/<int:pk>', detail_post, name='detail_post'),

]