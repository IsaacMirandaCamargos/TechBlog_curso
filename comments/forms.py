from django import forms
from comments.models import Comment


class CommentSubmitForm(forms.ModelForm):

    name_attrs = {"type":"text", "class":"form-control", "id":"nameInputComment"}
    email_attrs = {"type":"email", "class":"form-control", "id":"emailInputComment", "aria-describedby":"emailHelp"}
    text_attrs = {"class":"form-control", "id":"textAreaComment", "rows":"3"}
    

    name = forms.CharField(widget=forms.TextInput(attrs=name_attrs))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs=email_attrs))

    text = forms.CharField(widget=forms.TextInput(attrs=text_attrs))

    class Meta:

        model = Comment
        fields = ['name', 'email', 'text', 'post']
