
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

from blogs.models import Category, Blog, AboutUs, FollowUs


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status = 'Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status = 'Published').order_by('-updated_at')

    try:
        about_us = AboutUs.objects.get()
    except:
        about_us = None

    # try:
    #     follow_us = FollowUs.objects.all()
    # except:
    #     follow_us = None

    context = {
        "about_us": about_us,
        "featured_posts": featured_posts,
        "posts": posts,
    }
    return render(request, 'home.html', context)