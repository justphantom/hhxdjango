from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework import mixins, viewsets

from blog.models import Post
from .forms import CommentForm
from .serializers import CommentSerializer
from .models import Comment


# from .models import Comment

# Create your views here.


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request, messages.SUCCESS,
                             '评论发表成功', extra_tags='success')
    else:
        messages.add_message(request, messages.ERROR,
                             form.errors, extra_tags='danger')
    return redirect(post)


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
