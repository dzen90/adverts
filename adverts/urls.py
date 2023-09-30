from django.urls import path
from adverts import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

#app_name = 'adverts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.search, name='search'),
    path('advert/<int:pk>', views.AdvertView.as_view(), name='advert'),
    path('create', login_required(views.AdvertsCreateView.as_view()), name='create'),
    path('advert/<int:pk>/edit', login_required(views.AdvertUpdateView.as_view()), name='update'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('user/<slug:username>', views.UserView.as_view(), name='user'),
    path('user/<slug:username>/update', views.UserUpdateView.as_view(), name='user_update')
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT) 