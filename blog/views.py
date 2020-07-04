import markdown
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Post


# from django.http import HttpResponse


# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list, 'title': 'Blog'})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post, 'title': post.title})


def search(request):
    q = request.POST.get('q')
    if not q:
        error_msg = "请输入关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'post_list': post_list})
