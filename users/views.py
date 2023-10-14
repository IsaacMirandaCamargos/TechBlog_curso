from django.shortcuts import redirect, render

from users.forms import NewsletterSignupForm

# Create your views here.
def newsletter_signup(request):

    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return redirect('home')