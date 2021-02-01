from django.shortcuts import render

# Create your views here.

postList = [
    {
        'author': 'Shihab Uddin',
        'title': 'Blog Post One',
        'content': 'First Post Content',
        'date_posted': 'January 12, 2021',
    }, {
        'author': 'Shihab Uddin',
        'title': 'Blog Post Two',
        'content': 'Second Post Content',
        'date_posted': 'January 14, 2021',
    }
]


def home(request):
    context = {
        'posts': postList
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
