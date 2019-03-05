from django.db import models

# Create your models here.


class Movie(models.Model):
    """映射数据库表"""
    cover = models.URLField("封面", unique=True)
    url = models.URLField("链接", unique=True)
    title = models.CharField("电影标题", max_length=200)
    info = models.CharField("上演信息", max_length=300)
    rate = models.FloatField("评分", default=0)
    commit = models.CharField("短评", max_length=200)
