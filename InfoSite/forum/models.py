from django.contrib.auth.models import User
from django.db import models
from LK.models import Lkpage
from LK.models import Profile


class Comment(models.Model):
    post = models.ForeignKey(Lkpage, related_name='comments',default=None, null=True, blank=True, on_delete=models.CASCADE )
    author = models.ForeignKey(User,default=None, null=True, blank=True, on_delete=models.CASCADE )
    body = models.TextField('Комментарий')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.first_name, self.post)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'