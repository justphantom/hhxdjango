from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookIndexView.as_view(), name='index'),
]
