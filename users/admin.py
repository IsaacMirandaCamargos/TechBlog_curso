from django.contrib import admin
from .models import NewsletterUser, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(NewsletterUser)