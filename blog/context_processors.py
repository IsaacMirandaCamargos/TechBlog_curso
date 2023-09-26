from blog.models import Category, Tag, Post

def categories_and_tags(request):
    context = dict()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    for category in categories:
        count = Post.objects.filter(category=category.id).count()
        category.count = count

    last_posts = Post.objects.order_by('-created_at')[:3]

    context['last_posts'] = last_posts
    context['categories'] = categories
    context['tags'] = tags

    return context