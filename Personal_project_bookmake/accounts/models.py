from django.db import models

from django.contrib.auth.models import User

class Follow(models.Model):

    me = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    you = models.ForeignKey(User, on_delete=models.CASCADE,related_name='follower')

    def __str__(self):
        return self.me.username+" follow "+self.you.username

