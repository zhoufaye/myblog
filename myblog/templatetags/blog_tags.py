#coding:utf-8
from  ..models import Post,Category
from django import template
# 首先导入template 模板，然后实例化一个temlplate.Library()类，并将函数get_recent_posts 装饰为register.simple_tag(),
# 这样就可以在模板中使用语法{% get_recent_posts%} 来调用这个函数了
register=template.Library()
@register.simple_tag()

# 展示最新5篇文章的方法
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-create_time")[:num]

#归档方法
@register.simple_tag()
def archives():
    return Post.objects.dates("create_time","month",order='DESC')

#分类
@register.simple_tag()
def get_categories():
    return  Category.objects.all()

