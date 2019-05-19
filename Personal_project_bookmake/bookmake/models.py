from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bookmake(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=50)
    url = models.URLField('Site URL')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name + " : " + self.url

    class Meta:
        ordering = ['-site_name']