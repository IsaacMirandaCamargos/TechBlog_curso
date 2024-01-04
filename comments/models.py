from django.db import models
from blog.models import Post

# Create your models here.
class Comment(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField(max_length=600)
    is_valid = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name