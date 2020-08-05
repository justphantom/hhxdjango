from django.db import models

# Create your models here.
from django.urls import reverse


class Author(models.Model):
    name = models.CharField('作者', max_length=100)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BookInfo(models.Model):
    name = models.CharField('书籍', max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField('简介')
    create_time = models.DateTimeField('创建时间', auto_now=True)
    index = models.IntegerField('顺序', blank=True)

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
        return reverse("books:detail", kwargs={"index": self.index, "book_pk": self.book.pk})
