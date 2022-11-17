from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.post_list, name='post_list'),
    path('blog/<slug:slug>', views.post_detail, name='post_detail'),
    path('blog/doctor/add-post', views.add_post, name='add_post'),
    path('blog/doctor/posts', views.author_post_list, name='author_post_list'),
    path('blog/doctor/edit-post/<slug:slug>/<str:id>', views.edit_post, name='edit_post'),
    path('blog/doctor/delete-post/<slug:slug>/<str:id>', views.delete_post, name='delete_post'),
    path('blog/doctor/confirm-delete-post/<slug:slug>/<str:id>', views.confirm_delete_post, name='confirm_delete_post'),
]
