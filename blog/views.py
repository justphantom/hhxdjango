from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import AllowAny
from rest_framework import viewsets, mixins

from comments.serializers import CommentSerializer
from .models import Post
from .serializers import PostListSerializer, PostRetrieveSerializer
from comments.forms import CommentForm
from comments.models import Comment


class PostIndexView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 10

    # context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    # context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context.get('object')
        context['comment_form'] = CommentForm()
        # context['comment_list'] = Comment.objects.all()
        return context


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


class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostRetrieveSerializer
        else:
            return super().get_serializer_class()

    # permission_classes = [AllowAny]
    @action(
        methods=["GET"],
        detail=True,
        url_path="comments",
        url_name="comment",
        pagination_class=PageNumberPagination,
        serializer_class=CommentSerializer,
    )
    def list_comments(self, request, *args, **kwargs):
        post = self.get_object()
        queryset = post.comment_set.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
