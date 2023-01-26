from django.db import models

from autoslug import AutoSlugField


NULLABLE = {'blank': True, 'null': True}

class Record (models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = AutoSlugField(populate_from='title', verbose_name='Слуг')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='image/', **NULLABLE, verbose_name='Превью')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(verbose_name='Опубликовано', default=False)
    views_cntr = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.title

