from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.utils import format_body
from .models import Category, Post
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

# Create your views here.
def list_posts(request):
    context = dict()

    category_id = request.GET.get('category')
    
    if category_id:
        category_id = int(category_id)
        posts_list = Post.objects.filter(category=category_id).order_by('-created_at')
        category_search = Category.objects.get(pk=category_id)
        context['category_search'] = category_search
    else:
        posts_list = Post.objects.all().order_by('-created_at')

    for post in posts_list:
        post.mini_description = format_body(post.body, 10)

    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context['posts'] = posts

    return render(request, 'blog/posts-list.html', context=context)

def detail_post(request, pk):

    context = dict()

    post = Post.objects.get(pk=pk)
    context['post'] = post

    hit_count = HitCount.objects.get_for_object(post)
    HitCountMixin.hit_count(request, hit_count)


    return render(request, 'blog/post-detail.html', context=context)