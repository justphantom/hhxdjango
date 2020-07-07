import markdown
from django.contrib import messages
from django.db.models import Q
from django.views import generic
from .models import Post


# from django.http import HttpResponse


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    model = Post


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get(self, request, *args, **kwargs):
        reponse = super(DetailView, self).get(request, *args, **kwargs)
        self.object.increase_view()
        return reponse

    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        md = markdown.Markdown(
            extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])
        post.body = md.convert(post.body)
        return post

def search(request):
    q = request.POST.get('q')
    if not q:
        error_msg = "请输入关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'post_list': post_list})
