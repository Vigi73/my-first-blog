from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
        Модель для постов
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    text = models.TextField(verbose_name='Текст сообщения')
    create_date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    published_date = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
