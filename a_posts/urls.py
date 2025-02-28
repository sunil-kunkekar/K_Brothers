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
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)