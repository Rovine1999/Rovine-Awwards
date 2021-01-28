from . import views
from .views import ProjectCreateView
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path('home/', views.home, name='home'),
    path('post/new/',ProjectCreateView.as_view(), name='post'),
    re_path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    re_path('register/',views.register, name='registration'),
    path('accounts/profile/', views.profile, name='profile'),
    path('', views.awwards, name='awwards'),
    path('search/', views.search_awward, name='search_results'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)