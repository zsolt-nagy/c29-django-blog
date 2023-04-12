from django.shortcuts import render
from .models import Post

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


def new_post(request):
    if request.method == 'POST':
        try:
            new_post = Post.objects.create(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                content=request.POST.get('description'),
            )
            new_post.save()
            context = {
                'title': 'The post has been created.',
                'show_form': False,
            }
        except:
            context = {
                'title': 'Error creating post. Try again later.',
                'show_form': False,
            }
    else:
        context = {
            'title': 'New Post',
            'show_form': True,
        }
    return render(request, 'post/new_post.html', context)
