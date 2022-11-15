from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.post_list, name='post_list'),
    path('blog/<slug:slug>', views.post_detail, name='post_detail'),
    path('blog/doctor/add-post', views.add_post, name='add_post'),
    path('blog/doctor/edit-post/<slug:slug>/<str:id>', views.edit_post, name='edit_post'),
    path('blog/doctor/posts', views.author_post_list, name='author_post_list'),
]
