from django.db import models
from datetime import *

class ModelsNewsPage(models.Model):
    title = models.CharField('Название', max_length=100, default='')
    preview = models.CharField('Превью', max_length=300, default='')
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата', default=datetime.today())
    img = models.ImageField('Изображение', default=None, null=True, blank=True, upload_to='images')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'