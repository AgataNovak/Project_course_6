from django.db import models


class BlogPost(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Статус публикации')
    views_counter = models.IntegerField(verbose_name='Количество просмотров')
    