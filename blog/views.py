import markdown
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
# from django.views import generic
from .models import Post


# from django.http import HttpResponse


# Create your views here.
# class IndexView(generic.ListView):
#     model = Post
#     template_name = 'blog/index.html'


# class DetailView(generic.DetailView):
#     model = Post
#     template_name = 'blog/detail.html'
#     context_object_name = 'post'
#
#     def get_object(self, queryset=None):
#         post = super().get_object(queryset=None)
#         md = markdown.Markdown(
#             extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])
#         post.body = md.convert(post.body)
#         return post
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context.get(post.title, None)
#         print(context['title'])
#         return context


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list, 'title': 'MyBlog'})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_view()
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
