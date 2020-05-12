from django.views.generic import ListView
from ...models import Post


class PostTemplate(ListView):
    model = Post.objects.all().order_by("-date")[:25]
    template_name = 'blog/blog.html'
    context_object_name = 'blog_view'
