from django.shortcuts import render


# from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', context={
        'title': 'My Blog Home Page',
        'welcome': 'Welcome to my blog',
    })
