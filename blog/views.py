from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html', {})

def db_blog(request):
   blog = Blog.objects.all()
   return render(request, 'blog/blog.html', {'blogs': blog})