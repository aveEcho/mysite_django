# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField('标题', max_length=250, blank=True, null=True)
    # 这个字段将会在URLs中使用。slug就是一个短标签，该标签只包含字母，数字，下划线或连接线。
    slug = models.CharField(max_length=250, unique_for_date='publish')
    # 一篇帖子只能由一名用户编写，一名用户能编写多篇帖子
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField('发布时间', default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField('展示状态', max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
        # Django查询数据库的时候默认返回的是根据publish字段进行降序排列过的结果
        ordering = ('-publish',)

    def __unicode__(self):
        return self.title
