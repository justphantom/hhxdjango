import markdown
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
# from django.views import generic
from .models import Post
from comments.forms import CommentForm
from comments.models import Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostListSerializer


@api_view(http_method_names=["GET"])
def home(request):
    post_list = Post.objects.all()
    serializer = PostListSerializer(post_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list, 'title': 'Blog'})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_view()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    comment_form = CommentForm()
    comment_list = Comment.objects.filter(post=pk)
    comment_count = comment_list.count()
    return render(request, 'blog/detail.html', context={'post': post, 'title': post.title, 'comment_form': comment_form,
                                                        'comment_list': comment_list, 'comment_count': comment_count})


def search(request):
    q = request.POST.get('q')
    if not q:
        error_msg = "请输入关键词"
        messages.add_message(request, messages.ERROR,
                             error_msg, extra_tags='danger')
    post_list = Post.objects.filter(
        Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'post_list': post_list, 'title': 'Blog'})


def page_not_found(request, exception):
    return render(request, 'errors/404.html')
