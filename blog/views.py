from django.shortcuts import render
from blog.models import Category, Tag
from blog.utils import format_tag

# Create your views here.
def list_posts(request):
    context = dict()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    for tag in tags:
        tag.name = format_tag(tag.name)

    context['categories'] = categories
    context['tags'] = tags

    return render(request, 'blog/posts-list.html', context=context)

def detail_post(request, pk):
    context = dict()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    for tag in tags:
        tag.name = format_tag(tag.name)

    context['categories'] = categories
    context['tags'] = tags

    return render(request, 'blog/post-detail.html', context=context)