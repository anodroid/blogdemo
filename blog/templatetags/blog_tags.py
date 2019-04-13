from django import template
from django.utils import timezone
from django.db.models.aggregates import Count, Sum
from ..models import Post, Category, Tag, Visit

register = template.Library()

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def cate_list():
    return Category.objects.annotate(post_num=Count('post')).filter(post_num__gt=0)

@register.simple_tag
def tag_list():
    return Tag.objects.annotate(post_num=Count('post')).filter(post_num__gt=0)

@register.simple_tag
def dayly_count():
    date = timezone.now().date()
    daily_count = Visit.objects.filter(visit_date=date).aggregate(daily_count=Sum("count")).get('daily_count') or 0
    return daily_count

@register.simple_tag
def total_count():
    total_count = Visit.objects.all().aggregate(total_count=Sum("count")).get('total_count')
    return total_count

@register.simple_tag
def pos_num():
    return Post.objects.count()