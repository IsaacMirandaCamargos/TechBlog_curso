from django.shortcuts import redirect, render
from django.contrib import messages
from users.forms import NewsletterSignupForm

# Create your views here.
def newsletter_signup(request):

    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Seu e-mail foi cadastrado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Falha no cadastro por e-mail invalido ou e-mail já cadastrado!")
            return redirect('home')
    else:
        return redirect('home')