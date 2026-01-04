from django.http import HttpResponse
from blogs.models import Category, Blog
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status = 'Published', category = category_id)

    #use try/except to do some actions if the category doesn't exist
    try:
        category = Category.objects.get(pk = category_id)
    except:
        #redirect the user to homepage
        return redirect('home')

    #shoe 404 page if the category doesn't exist
    # category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
