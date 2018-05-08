# coding:utf-8

from django.db import models

# Create your models here.

class People(models.Model):
    fenzu_choices = (
        ('佳佳', '佳佳'),
        ('木木', '木木'),
        ('绾绾', '绾绾'),
    )
    shifouchoucha_choices = (
        ('是', '是'),
        ('否', '否'),
    )
    fenzu = models.CharField(u'所属分组', max_length=20, null=True, choices=fenzu_choices)
    title = models.CharField(u'昵称', max_length=256, null=True)
    content = models.IntegerField(u'未交次数', null=True, default='0')
    shifouchoucha = models.CharField(u'是否抽查', max_length=10, null=True, choices=shifouchoucha_choices, default='是')
    # pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    # update_time = models.DateTimeField(u'更新时间', auto_now = True, null = True)
    def __str__(self):
        return self.title

# class UserInfo(models.Model):
#     user = models.CharField(max_length=32)
#     pwd = models.CharField(max_length=32)
#     def __str__(self):
#         return self.user