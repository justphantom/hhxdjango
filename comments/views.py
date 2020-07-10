from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from blog.models import Post
from .forms import CommentForm
from .models import Comment


# Create your views here.


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment()
        comment.name = form.cleaned_data.get('name')
        comment.email = form.cleaned_data.get('email')
        comment.url = form.cleaned_data.get('url')
        comment.text = form.cleaned_data.get('text')
        comment.post = post
        comment.save()
        messages.add_message(request, messages.SUCCESS, '评论发表成功', extra_tags='success')
        return redirect(post)
    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request, messages.ERROR, '评论发表失败', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)
