# -*- coding: utf8 -*-
from django.db import models

class Topic(models.Model):
    # 主旨
    subject = models.CharField(max_length=255)
    # 內容
    content = models.TextField()
    # 發表者
    poster = models.CharField(max_length=20)
    # 發表日期
    publication_date = models.DateTimeField(auto_now_add=True)
    # 回覆日期
    reply_date = models.DateTimeField(auto_now_add=True)
class Reply(models.Model):
    # 回覆主題
    topic_id = models.IntegerField(default=0)
    # 回覆內容
    content = models.TextField()
    # 發表者
    poster = models.CharField(max_length=20)
    # 發表日期
    publication_date = models.DateTimeField(auto_now_add=True)