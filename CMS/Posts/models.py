from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

status = (('Public','Public'),('Private','Private'))

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    content = models.TextField(max_length=250)
    owner = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='Public', choices=status)

    def __str__(self):
        return f"id:{self.id},Title:{self.title},Desc:{self.description},Content:{self.content},Owner:{self.owner},Created_at:{self.created_at},Updated_at:{self.updated_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Posts"

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"User:{self.user},Post:{self.user},created:{self.user},"

    class Meta:
        verbose_name_plural = 'PostLikes'



