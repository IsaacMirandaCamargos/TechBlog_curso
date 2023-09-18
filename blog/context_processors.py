from blog.models import Category, Tag
from blog.utils import format_tag

def categories_and_tags(request):
    context = dict()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    context['categories'] = categories
    context['tags'] = tags

    return context