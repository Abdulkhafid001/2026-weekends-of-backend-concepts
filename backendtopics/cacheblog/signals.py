from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog


@receiver(post_save, sender=Blog)
def clear_recent_posts_cache(sender, **kwargs):
    cache.delete('recent-posts')
