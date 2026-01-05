from blogs.models import Category, FollowUs

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)

def get_follow_us(request):
    follow_us = FollowUs.objects.all()
    return dict(follow_us = follow_us)