# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.template import Library
from django.utils.html import format_html
from django_blog.models import Post
from django_blog.forms import PostForm

register = Library()

@register.simple_tag
def all_posts():
    posts = Post.objects.all()
    return posts 

@register.inclusion_tag('_new_post_form.html')
def new_post():
    url =  reverse('django_blog:post', current_app='django_blog')
    
    context =  {
        'form': PostForm(), 
        'action': url
    }
    return context