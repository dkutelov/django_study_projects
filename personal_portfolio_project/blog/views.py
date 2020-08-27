from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def all_blogs(request):
    posts_count = BlogPost.objects.all().count
    posts = BlogPost.objects.order_by('-post_date')[:5]
    return render(request, 'blog/all_blogs.html', {'posts': posts, 'posts_count': posts_count})


def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

