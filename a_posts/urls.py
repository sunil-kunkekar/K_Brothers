from django.urls import path
from a_posts.views import *

urlpatterns = [
    path('create/', post_create_view, name='post-create'),
    path('delete/<pk>/', post_delete_view, name='post-delete'),
    path('edit/<pk>/',edit_post_view, name='post-edit'),
    
]