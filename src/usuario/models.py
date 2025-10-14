from django.db import models
from django.contrib.auth.models import User


def user_avatar_path(instance, filename):
    # Use dated path similar to migration so uploaded files match migration expectations
    return f'usuarios/%Y/%m/%d/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='usuarios/%Y/%m/%d', blank=True, null=True)
    location = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
