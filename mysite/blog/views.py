from django.shortcuts import render
from blog.models import Post


def blog(request):
    params = {'data': list(Post.objects.all().order_by("-date")[:25])}
    return render(request, 'blog/blog.html', params)
