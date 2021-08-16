from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Comments(models.Model):
    comment_name = models.CharField(max_length=150)
    comment_email = models.EmailField()
    comment = models.TextField()
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment_date = models.DateTimeField(default=timezone.now)
    comment_published = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_name