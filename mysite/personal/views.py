from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'context': ['Contact me @', 'yogeshseralia@email.com']})


def blog(request):
    return render(request, 'blog/blog.html')