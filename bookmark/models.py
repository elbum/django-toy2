from django.db import models

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return "야호 %s %s 야호" % (self.title, self.url)
