from django import template

register = template.Library()

from blog.models import Post

@register.simple_tag
def getPostAuthorName(post):
    if(post.created_by is None):
        name = 'Anonymous'
    else:
        author = post.created_by
        name = author.name
    return name