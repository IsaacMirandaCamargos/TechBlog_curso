from django.contrib import admin
from blog.models import Category, Post, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)