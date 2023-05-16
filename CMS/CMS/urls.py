from django.contrib import admin
from django.urls import path, include
from Posts.views import PostSerializer, PostApi
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostApi, 'post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Auth.urls')),
    path('post/', include(router.urls)), 
    path('post/', include('Posts.urls')), 
    path('auth/token/', obtain_auth_token)
]
