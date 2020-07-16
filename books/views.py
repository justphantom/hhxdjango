from django.db.models import Q
from django.shortcuts import render, get_object_or_404
# from django.views import generic
from .models import BookInfo, Chapter
import markdown


# Create your views here.
def index(request):
    book_list = BookInfo.objects.all()
    return render(request, 'books/index.html', context={'book_list': book_list, 'title': 'Book', })


def chapter(request, book_pk):
    chapter_list = Chapter.objects.filter(book=book_pk)
    book_title = BookInfo.objects.get(pk=book_pk).name
    return render(request, 'books/chapter.html', context={'chapter_list': chapter_list, 'title': book_title, })


def detail(request, book_pk, index):
    chapter = get_object_or_404(Chapter, Q(book=book_pk), Q(index=index))
    chapter.body = markdown.markdown(chapter.body)
    return render(request, 'books/detail.html', context={'chapter': chapter, 'title': chapter.title, })
