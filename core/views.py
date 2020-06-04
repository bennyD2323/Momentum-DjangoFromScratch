from django.shortcuts import render
from .models import CodeSnippet
from .models import Tag

# Create your views here.


def homepage(request):
    

    return render(request, 'snippets/home.html')