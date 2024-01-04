from django.urls import path, include
from .views import comment_submit

urlpatterns = [
    path('submit_comment', comment_submit, name='comment_submit')
]