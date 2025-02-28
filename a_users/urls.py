from django.urls import path
from a_users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/edit/',profile_edit_view, name='profile-edit'),
    path('<username>/', profile_view, name="userprofile"),
    path('profile/delete/',profile_delete_view, name='profile-delete'),
    path('profile/onboarding/', profile_edit_view, name="profile-onboarding"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)