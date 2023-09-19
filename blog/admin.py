from typing import Any
from django.contrib import admin
from django.forms import ModelForm
from blog.models import Category, Post, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
#admin.site.register(Post)

class PostAdminForm(ModelForm):

    class Meta:
        models = Post
        fields = ('title', 'category', 'tags', 'body', 'feature_image')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_author_name', 'title', 'created_at')
    form = PostAdminForm

    def full_author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    full_author_name.short_description = "author"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)