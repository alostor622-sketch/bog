from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Напиши что-нибудь')
    anons = models.CharField('Анонс', max_length=250)
    full_next = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/news/{self.id}'

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'новости'