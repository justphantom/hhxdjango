from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
