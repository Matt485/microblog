from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Post, TextPost, AudioPost, Blog

from django.contrib import messages
from django.contrib.auth import login

def index(request):
    latest_posts_list = Post.objects.all()
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'fragment/index.html', context)

def blog(request, blog_name):
    blog = get_object_or_404(Blog, blog_name=blog_name)
    context = {'blog_name': blog_name}
    return render(request, 'fragment/blog.html', context)

def blog_archive(request, blog_name):
    blog = get_object_or_404(Blog, blog_name=blog_name)
    context = {'blog_name': blog_name}
    return render(request, 'fragment/blog.html', context)

def blog_about(request, blog_name):
    blog = get_object_or_404(Blog, blog_name=blog_name)
    context = {'blog_name': blog_name}
    return render(request, 'fragment/blog.html', context)


def contact_page(request):
    latest_posts_list = Post.objects.all()
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'fragment/index.html', context)

def about_page(request):
    latest_posts_list = Post.objects.all()
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'fragment/index.html', context)

def help_page(request):
    latest_posts_list = Post.objects.all()
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'fragment/index.html', context)

def privacy_policy(request):
    latest_posts_list = Post.objects.all()
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'fragment/index.html', context)

def faq_page(request):
    latest_posts_list = Post.objects.all()
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'fragment/index.html', context)
