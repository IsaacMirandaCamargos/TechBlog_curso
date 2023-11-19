from django.core.mail import EmailMessage
import os
from django.utils.text import slugify
from blog.models import Post

def get_next_post_id(request_id):
    next_posts = Post.objects.filter(id__gt=request_id).order_by("id")[:1]
    if next_posts:
        return next_posts.get().id

def get_previous_post_id(request_id):
    previous_posts = Post.objects.filter(id__lt=request_id).order_by("-id")[:1]
    if previous_posts:
        return previous_posts.get().id


def format_body(body, num_words):

    body = body.split("</p>")[0]
    body = body.replace('<p class="mb-4 text-gray-700">', '')
    body = body.replace("<p>", "")
    body = body.split(" ")[:num_words]
    body = " ".join(body).strip(".") + " ..."
    return body

def send_new_post_email(emails, post):
    email_message = EmailMessage(
        subject="Bem vindo ao TECH Blog",
        body="Aproveite para aprender enquanto se aventura.",
        to=emails,
        from_email=os.getenv("SENDINBLUE_EMAIL_HOST")
    )
    email_message.template_id = 3

    email_message.merge_global_data = {
        "post_title": post.title,
        "post_body": format_body(post.body, 50),
        "post_id": post.id,
        "base_url": os.getenv("BASE_URL")
    }

    email_message.send()