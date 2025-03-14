from django.urls import path
from a_posts.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create/', post_create_view, name='post-create'),
    path('delete/<pk>/', post_delete_view, name='post-delete'),
    path('edit/<pk>/',edit_post_view, name='post-edit'),
    
    path('detail_post_page/<pk>/',post_detail_page_view, name='post'),
    path('category/<tag>/',home_view, name='category'),
    
    path('comment_sent/<pk>/', comment_sent, name='comment-sent'),
    path('comment/delete/<pk>/',comment_delete_view, name='comment-delete'),
    
    path('reply-sent/<pk>/',reply_sent, name='reply-sent'),
    path('reply/delete/<pk>/',reply_delete_view, name='reply-delete'),
    path('post/like/<pk>/', like_post, name="like-post"), 
    path('post/<pk>/', post_detail_page_view, name="post"), 
    
    path('comment/like/<pk>/', like_comment, name="like-comment"), 
    path('reply/like/<pk>/', like_reply, name="like-reply"),
    # path('post/<pk>/like/',like_post,name='like-post'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)