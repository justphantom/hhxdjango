from django.db import models

# Create your models here.
from django.urls import reverse


class BookInfo(models.Model):
    name = models.CharField('书籍', max_length=200)
    author = models.CharField('作者', max_length=50)
    description = models.TextField('简介')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:chapter", kwargs={"book_pk": self.pk})


class Chapter(models.Model):
    title = models.CharField('标题', max_length=200)
    index = models.IntegerField('顺序')
    body = models.TextField('正文')
    book = models.ForeignKey(
        BookInfo, verbose_name='书籍', on_delete=models.CASCADE)
    parent = models.IntegerField('上级章节', default=0)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk, "book_pk": self.book.pk})
