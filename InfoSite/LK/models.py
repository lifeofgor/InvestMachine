from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', default=None, null=True, blank=True, upload_to='images')
    telegram = models.CharField('Телеграмм', max_length=100, default=None, null=True)
    VK = models.CharField('ВК', max_length=100, default='')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Личный профиль'
        verbose_name_plural = 'Личные профили'


class Lkpage(models.Model):
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
    img_page = models.ImageField('Изображение', default=None, null=True, blank=True, upload_to='images')
    title_page = models.CharField('Название',default=None, null=True, blank=True, max_length=100)
    preview_page = models.CharField('Превью',default=None, null=True, blank=True, max_length=300)
    text_page = models.TextField('Статья')
    data_page = models.DateTimeField('Дата', default=timezone.now())

    def __str__(self):
        return self.title_page


    class Meta:
        verbose_name = 'Запись в форум'
        verbose_name_plural = 'Записи в форум'







