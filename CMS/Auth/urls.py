from django.urls import path
from .views import UserGenericView


urlpatterns = [
    path('user/', UserGenericView.as_view())
]