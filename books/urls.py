from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>', views.chapter, name='chapter'),
    path('<int:book_pk>/chapter/<int:index>', views.detail, name='detail'),
]
