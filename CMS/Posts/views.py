from rest_framework import viewsets, views, response
from .serializers import PostSerializer, Post, PostLike, PostLikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrAdmin
from django.db.models import Count, Q


class PostApi(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdmin]
    authentication_classes = [TokenAuthentication]
    queryset = Post.objects.all()

    def list(self, request, *args, **kwargs):
        inner_joined_data = Post.objects.prefetch_related('likes').annotate(like = Count('likes')).filter(Q(status='Public') | Q(owner=request.user)) 
        print('---->innerJOin-', inner_joined_data)
        serializer = PostSerializer(inner_joined_data, many=True)
        return response.Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Q(id=kwargs['pk']) & Q(owner=request.user)-> gives access to only owner
        else exception raises Post.DoesNotExist.
        when exception raises that means owner 

        """
        # self.check_object_permissions(request, data)
        try:
            data = Post.objects.prefetch_related('likes').annotate(like = Count('likes')).get(Q(id=kwargs['pk']) & Q(owner=request.user))
            
        except Post.DoesNotExist:
            return response.Response(data={"details":{}})

        serializer = PostSerializer(data)
        return response.Response(data=serializer.data)

class PostLikeApi(views.APIView):
    permission_classes = [IsOwnerOrAdmin]
    authentication_classes = [TokenAuthentication]

    def post(self, request, pk):
        already_liked = len(PostLike.objects.filter(user=request.user, post=pk))
        if already_liked > 0:
            like = PostLike.objects.get(user=request.user.id, post=pk)
            like.delete()
            return response.Response(data={"details":"like removed"})
        else:
            serializer = PostLikeSerializer(data={'post':pk},context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return response.Response(data=serializer.data)
            else:
                return response.Response(data=serializer.errors)
            

