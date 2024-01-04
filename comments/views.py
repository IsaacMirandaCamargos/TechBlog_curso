from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from django.contrib import messages
from comments.forms import CommentSubmitForm

# Create your views here.
def comment_submit(request):

    if request.method == 'POST':
        form = CommentSubmitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentário postado com sucesso!")
            return redirect(f'/blog/posts/{request.POST.get("post")}')
        else:
            messages.error(request, "Falha na postagem do comentáro!")
            return redirect(f'/blog/posts/{request.POST.get("post")}')
    else:
        return HttpResponseServerError()