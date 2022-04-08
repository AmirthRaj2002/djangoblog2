from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Comments
# Create your views here.
def index(request):
    post=Post.Newmanager.all()
    return render(request,'meetups/index.html',{'post':post})

def page(request,title):
    comment=Comments.filter(post=title)
    return render(request,'meetups/posts.html',{'com':comment})

def post_single(request,post):
    post=get_object_or_404(Post,title=post)
    return render(request,'meetups/posts.html',{'post':post})