# from django import template
# from ..models import Post
# from django.db.models import Count
# from django.utils.safestring import mark_safe
# import markdown
#
#
# register = template.Library()
#
#
# # get the recent posts
# @register.inclusion_tag('blog/post/latest_post.html')
# def show_latest_posts(count=5):
#     latest_posts = Post.published.order_by('-publish')[:count]
#     return {'latest_posts': latest_posts}
#
#
# # getting HTML markdowns
# @register.filter(name='markdown')
# def markdown_format(text):
#     return mark_safe(markdown.markdown(text))