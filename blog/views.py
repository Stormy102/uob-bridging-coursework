from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    post_numbers = Post.objects.all().count()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'post_count': post_numbers})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def handler404(request, exception):
    return render(request, 'blog/404.html', status=404)
