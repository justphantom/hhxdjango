from django.views import generic
from .models import BookInfo


class BookIndexView(generic.ListView):
    model = BookInfo
    template_name = 'books/index.html'
