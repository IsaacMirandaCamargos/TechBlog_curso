from django.shortcuts import render


# Create your views here.
def list_posts(request):
    return render(request, 'blog/posts-list.html')

def detail_post(request, pk):
    return render(request, 'blog/post-detail.html')