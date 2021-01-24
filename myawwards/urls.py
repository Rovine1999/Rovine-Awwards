from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
 re_path('register/',views.register, name='registration'),
    path('profile/',views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)