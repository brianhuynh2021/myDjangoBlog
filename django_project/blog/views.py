from django.shortcuts import render
from .models import Post 
# from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Brian',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 22, 2021'
    },
    {
        'author': 'Viet_lon',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2021'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})