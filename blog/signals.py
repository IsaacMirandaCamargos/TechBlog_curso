from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Post
from users.models import NewsletterUser
from blog.utils import send_new_post_email



@receiver(post_save, sender=Post)
def send_new_post_email_signal(sender, instance, **kwargs):
    emails = [user.email for user in NewsletterUser.objects.filter(active=True)]
    send_new_post_email(emails, instance)