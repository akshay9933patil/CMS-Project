from rest_framework import views
from .serializers import User, UserSerializer
from rest_framework.generics import CreateAPIView


class UserGenericView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
