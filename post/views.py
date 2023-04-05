from django.shortcuts import render
from .models import Post

# Create your views here.


# Create your views here.

def index(request):
    return render(request, 'template.html')


def post(request):
    post_count = Post.objects.all().count()
    context = {
        'count': post_count,
    }
    return render(request, 'post/post.html', context)
