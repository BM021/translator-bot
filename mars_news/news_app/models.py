from django.db import models

# импорт модели User для создания таблицы UserProfile
from django.contrib.auth.models import User

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=500)
    tags = models.CharField(max_length=60)
    image = models.ImageField(upload_to='news_app/media')
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self) -> str:
        return self.title
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self) -> str:
        return self.user.first_name







