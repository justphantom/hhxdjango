from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:book_pk>', views.ChapterView.as_view(), name='chapter'),
    path('<int:book_pk>/chapter/<int:pk>', views.DetailView.as_view(), name='detail'),
]
