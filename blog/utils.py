from django.core.mail import EmailMessage
import os
from django.utils.text import slugify

def format_tag(tag):
    tag = slugify(tag)
    tag = tag.replace("-", "")
    tag = "#" + tag
    return tag

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