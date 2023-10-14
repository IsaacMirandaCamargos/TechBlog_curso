from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.utils import format_body
from .models import Category, Post, Tag
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

# Create your views here.
def get_filtered_posts(category_id=None, tag_id=None, text_search=None):
    filters = {}

    if category_id:
        filters['category'] = int(category_id)
    if tag_id:
        filters['tags__id'] = [int(tag_id)]
    if text_search:
        filters['title__icontains'] = text_search

    return Post.objects.filter(**filters).order_by('-created_at')
    
def list_posts(request):
    context = dict()

    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')
    text_search = request.GET.get('search')
    
    posts_list = get_filtered_posts(category_id, tag_id, text_search)

    if category_id:
        context['category_search'] = Category.objects.get(pk=int(category_id))
    if tag_id:
        context['tag_search'] = Tag.objects.get(pk=int(tag_id))
    if text_search:
        context['text_search'] = text_search

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