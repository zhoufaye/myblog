#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import  python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    create_time=models.DateTimeField()  # 时间类型
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=200,blank=True) # 文章摘要，可以没有文章摘要，CharField 默认情况下，不为空，blank=True ，表示可以为空
    category=models.ForeignKey(Category)  # 一篇文章，只有一个分类，但是一个分类可以有多篇文章，ForeignKey 表示一对多关系
    tag=models.ManyToManyField(Tag,blank=True)  # 一个文章可以有多个标签，同一个标签可能也有多个文章，同时规定文章可以没有标签，所以blank=True

    author=models.ForeignKey(User) # 文章作者，这里User 是从django.contrib.auth.models 导入的，规定一个文章可以有一个作者，但是一个作者可以有多个文章
    def __str__(self):
        return self.title
    # 自定义get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('myblog:detail',kwargs={'pk',self.pk})







