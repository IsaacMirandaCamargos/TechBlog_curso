from blog.models import Category, Tag, Post
from blog.utils import format_body
from hitcount.models import HitCount

def categories_and_tags(request):
    context = dict()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    for category in categories:
        count = Post.objects.filter(category=category.id).count()
        category.count = count

    last_posts = Post.objects.order_by('-created_at')[:3]
    for lpost in last_posts:
        lpost.mini_description = format_body(lpost.body)

    hits = HitCount.objects.all()[:3]
    object_pks = [hit.object_pk for hit in hits]
    most_viewed = [Post.objects.get(pk=pk) for pk in object_pks]
    
    context['most_viewed'] = most_viewed
    context['last_posts'] = last_posts
    context['categories'] = categories
    context['tags'] = tags

    return context