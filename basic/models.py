from django.db import models


# Create your models here.


class ProcessInfo(models.Model):
    processno = models.CharField('工序编号', max_length=20)
    processname = models.CharField('工序名称', max_length=100)
    createtime = models.DateTimeField('创建时间', auto_now_add=True)
    modifytime = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '工序信息'
        verbose_name_plural = verbose_name
        ordering = ['processno']

    def __str__(self):
        return self.processname
