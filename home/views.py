from django.shortcuts import render
from blog.models import MainFeaturedPost
from blog.utils import format_body

# Create your views here.
def home(request):
    context = dict()

    main_featured_posts = MainFeaturedPost.objects.filter(active=True)[:3]
    for mfpost in main_featured_posts:
        mfpost.post.mini_description = format_body(mfpost.post.body, 20)

    context['main_featured_posts'] = main_featured_posts

    return render(request, 'blog/index.html', context=context)