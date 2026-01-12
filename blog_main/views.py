from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect

from blog_main.forms import RegisterForm
from blogs.models import Category, Blog, AboutUs, FollowUs, User


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



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form})
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')