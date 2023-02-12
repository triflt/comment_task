from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def home_reviews(request):
    reviews = Article.objects.all()
    return render(request, 'reviews/home_reviews.html', {'reviews': reviews})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Invalid input'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'reviews/create.html', data)
