from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from accommodation.models import Category
from content.models import Content, CImages
from home.models import Settings


def index(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    content = Content.objects.filter(type='blog')
    lastContent = Content.objects.filter(type='blog').order_by('-id')[:3]
    context = {'setting': setting,
               'category': category,
               'content': content,
               'lastContent': lastContent,
               'page': 'content',
               }
    return render(request,'content_blog_archive.html',context)


def content_detail(request,id,slug):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    content = Content.objects.get(pk=id)
    images = CImages.objects.filter(content_id=id)
    lastContent = Content.objects.filter(type='blog').order_by('-id')[:2]
    context = {'setting': setting,
               'category': category,
               'content': content,
               'images': images,
               'lastContent': lastContent,
               'page': 'content',
               }
    return render(request, 'content_detail.html', context)