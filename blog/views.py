from django.shortcuts import render
from .models import Post

# Create your views here.
def list_posts(request):
    return render(request, 'blog/posts-list.html')

def detail_post(request, pk):

    context = dict()

    post = Post.objects.get(pk=pk)
    context['post'] = post

    return render(request, 'blog/post-detail.html', context=context)