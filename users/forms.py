from django import forms
from users.models import NewsletterUser

class NewsletterSignupForm(forms.ModelForm):

    email_attrs = {"type":"text",
                   "class":"form-control py-3",
                   "placeholder":"Digite seu e-mail",
                "aria-label":"Digite seu e-mail...",
                "aria-describedby":"button-addon2"}
    
    email = forms.EmailField(widget=forms.EmailInput(attrs=email_attrs))

    class Meta:

        model = NewsletterUser
        fields = ['email']
