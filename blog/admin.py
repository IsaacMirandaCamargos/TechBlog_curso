from django.contrib import admin
from blog.models import Category, Post, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
#admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_author_name', 'title', 'created_at')

    def full_author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    full_author_name.short_description = "author"