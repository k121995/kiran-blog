from blogapp.models import Post
from django.db.models import Count
from django import template
register=template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.inclusion_tag('latest_post123.html')
def show_latest_post():
    latest_post=Post.objects.order_by('-publish')[:4]
    return {'latest_post':latest_post,}
