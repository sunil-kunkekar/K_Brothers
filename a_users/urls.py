from django.urls import path
from a_users.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)