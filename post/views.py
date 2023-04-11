from django.shortcuts import render
from .models import Post

# Create your views here.


# Create your views here.

def index(request):
    context = {
        'title': 'blog home',
    }
    return render(request, 'post/home.html', context)


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'count': posts.count(),
        'title': 'posts',
    }
    return render(request, 'post/posts.html', context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'post/post.html', context)
