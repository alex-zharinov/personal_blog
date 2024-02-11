from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Blog(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField('Имя записи', max_length=200)
    text = models.TextField()
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=False)
