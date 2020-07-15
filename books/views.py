from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BookInfo, Chapter
import markdown


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'books/index.html'
    model = BookInfo


class ChapterView(generic.ListView):
    model = Chapter
    template_name = 'books/chapter.html'

    def get_queryset(self):
        book = get_object_or_404(BookInfo, pk=self.kwargs.get('book_pk'))
        return super(ChapterView, self).get_queryset().filter(book=book)


class DetailView(generic.DetailView):
    model = Chapter
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['title'] = context.get('title')
        return context
