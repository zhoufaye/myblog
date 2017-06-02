#coding:utf-8
from django.contrib import admin
from .models import Post,Category,Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','category','author']
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)


