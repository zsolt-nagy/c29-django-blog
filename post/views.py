from django.shortcuts import render
from .models import Post

# Create your views here.


# Create your views here.

def index(request):
    context = {
        'title': 'blog home',
    }
    return render(request, 'post/home.html', context)


def post(request):
    post_count = Post.objects.all().count()
    context = {
        'count': post_count,
        'title': 'posts',
    }
    return render(request, 'post/post.html', context)
