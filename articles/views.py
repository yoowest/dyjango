from django.shortcuts import render
from .models import Article

# Create your views here.
def blogs (request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/blogs.html', { 'articles': articles })
