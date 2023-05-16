from rest_framework import serializers
from .models import Post, PostLike, User
from django.utils import timezone

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(default=serializers.CurrentUserDefault())
    like = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "content",
            "owner",
            "created_at",
            "updated_at",
            "status",
            "like"
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.status = validated_data.get('status', instance.status)
        instance.created_at = instance.created_at
        print('status -------->>>',validated_data.get('status'))
        print('created at -------->>>',validated_data.get('created_at'))
        print('updated at -------->>>',validated_data.get('updated_at'))
        print('current time -------->>>',)
        instance.updated_at = timezone.now()
        instance.save()
        return instance
    
class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PostLike
        fields = '__all__'

    


