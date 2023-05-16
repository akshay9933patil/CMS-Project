from django.urls import path
from .views import PostLikeApi

urlpatterns = [
    path('post_like/<int:pk>/', PostLikeApi.as_view())
]