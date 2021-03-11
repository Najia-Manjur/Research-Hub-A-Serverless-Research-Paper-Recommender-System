from django.shortcuts import render
from .models import Post   #from models,py in out current folder, import Post table


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'webapp/home.html', context)


def about(request):
    return render(request, 'webapp/about.html', {'title': 'About'})