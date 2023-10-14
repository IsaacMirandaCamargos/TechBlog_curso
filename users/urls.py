from django.urls import path, include
from .views import newsletter_signup

urlpatterns = [
    path('signup_newsletter', newsletter_signup, name='newsletter_signup')
]