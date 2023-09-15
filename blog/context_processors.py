from blog.models import Category, Tag
from blog.utils import format_tag

def categories_and_tags(request):
    context = dict()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    for tag in tags:
        tag.name = format_tag(tag.name)

    context['categories'] = categories
    context['tags'] = tags

    return context