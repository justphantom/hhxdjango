from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostIndexView.as_view(), name='index'),
    path('<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('search/', views.search, name='search'),
]
