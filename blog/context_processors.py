from blog.models import Category, Tag, Post, FooterFeaturedPost
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
        lpost.mini_description = format_body(lpost.body, 18)

    hits = HitCount.objects.all()[:3]
    object_pks = [hit.object_pk for hit in hits]
    most_viewed = [Post.objects.get(pk=pk) for pk in object_pks]

    footer_featured_posts = FooterFeaturedPost.objects.filter(active=True)[:3]
    for ffpost in footer_featured_posts:
        ffpost.post.mini_description = format_body(ffpost.post.body, 7)

    context['footer_featured_posts'] = footer_featured_posts
    context['most_viewed'] = most_viewed
    context['last_posts'] = last_posts
    context['categories'] = categories
    context['tags'] = tags

    return context