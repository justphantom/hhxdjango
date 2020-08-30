from django.db import models


# Create your models here.


class ProcessInfo(models.Model):
    code = models.CharField('工序编号', max_length=20)
    name = models.CharField('工序名称', max_length=100)
    createtime = models.DateTimeField('创建时间', auto_now_add=True)
    modifytime = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '工序信息'
        verbose_name_plural = verbose_name
        ordering = ['code']

    def __str__(self):
        return self.name


class ProductType(models.Model):
    code = models.CharField('类型编号', max_length=10)
    name = models.CharField('类型名称', max_length=20)
    createtime = models.DateTimeField('创建时间', auto_now_add=True)
    modifytime = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '产品类型'
        verbose_name_plural = verbose_name
        ordering = ['code']

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    code = models.CharField('产品编号', max_length=20)
    name = models.CharField('产品名称', max_length=50)
    model = models.CharField('产品型号', max_length=50)
    type = models.ForeignKey(ProductType, verbose_name='产品类型', on_delete=models.PROTECT)
    createtime = models.DateTimeField('创建时间', auto_now_add=True)
    modifytime = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name
        ordering = ['code']

    def __str__(self):
        return self.name
