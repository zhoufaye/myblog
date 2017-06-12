#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import  python_2_unicode_compatible
from DjangoUeditor.models import  UEditorField
# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name=models.CharField(verbose_name="分类名",max_length=100)
    class Meta:
        verbose_name="分类"
        verbose_name_plural="分类"
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Tag(models.Model):
    name=models.CharField(verbose_name="标题名",max_length=100)
    class Meta:
        verbose_name="标签"
        verbose_name_plural="标签"
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Post(models.Model):
    title=models.CharField(max_length=100,verbose_name="标题")
 #   body=models.TextField()

    create_time=models.DateTimeField(verbose_name="发布时间")  # 时间类型
    modified_time=models.DateTimeField(verbose_name="修改时间")
    excerpt=models.CharField(max_length=200,blank=True,verbose_name="摘要") # 文章摘要，可以没有文章摘要，CharField 默认情况下，不为空，blank=True ，表示可以为空
    category=models.ForeignKey(Category,verbose_name="分类")  # 一篇文章，只有一个分类，但是一个分类可以有多篇文章，ForeignKey 表示一对多关系
    tag=models.ManyToManyField(Tag,blank=True,verbose_name="标签")  # 一个文章可以有多个标签，同一个标签可能也有多个文章，同时规定文章可以没有标签，所以blank=True

    author=models.ForeignKey(User,verbose_name="作者") # 文章作者，这里User 是从django.contrib.auth.models 导入的，规定一个文章可以有一个作者，但是一个作者可以有多个文章
    body =UEditorField(u'内容	',width=1000, height=600, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000})

    class Meta:
        verbose_name="文章"
        verbose_name_plural="文章"

    def __str__(self):
        return self.title
    # 自定义get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('myblog:detail',kwargs={'pk':self.pk})








