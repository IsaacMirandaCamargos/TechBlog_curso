from django.shortcuts import render
from .models import Post
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

# Create your views here.
def list_posts(request):
    return render(request, 'blog/posts-list.html')

def detail_post(request, pk):

    context = dict()

    post = Post.objects.get(pk=pk)
    context['post'] = post

    hit_count = HitCount.objects.get_for_object(post)
    HitCountMixin.hit_count(request, hit_count)


    return render(request, 'blog/post-detail.html', context=context)