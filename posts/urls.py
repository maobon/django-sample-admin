"""
URL configuration for posts
"""
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    path('', views.posts_list, name='list'),

    path('post-new', views.post_new, name='post-new'),

    # person.slug convert to path's params -> sample
    # < instance's filed waite to convert : param's name >
    path('<slug:param>', views.post_page, name='post_page'),
]
