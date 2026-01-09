from django.urls import path
from .views import NewsletterSubscribeView

app_name = 'newsletter'

urlpatterns = [
    path('', NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
]



