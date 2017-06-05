from django.shortcuts import render
from  django.shortcuts import get_object_or_404
from .models import Post
import markdown
# Create your views here.
def index(request):
    post_list=Post.objects.all().order_by('-create_time')
    return render(request,'myblog/index.html',context={'post_list':post_list})
def details(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.body=markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request,'myblog/detail.html',context={"post":post})







