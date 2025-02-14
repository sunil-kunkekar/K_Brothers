
from django.urls import path
from a_posts.views import *

urlpatterns = [
    path('create/', post_create_view, name='post-create'),
]