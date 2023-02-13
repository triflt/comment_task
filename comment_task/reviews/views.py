from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from .generate import sent2vec_generate, rating_predict, emotion_predict


def home_reviews(request):
    reviews = Article.objects.all()
    return render(request, 'reviews/home_reviews.html', {'reviews': reviews})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            rev = form.cleaned_data['review']
            vec = sent2vec_generate(rev)
            rating = round(rating_predict(vec), 1)
            emotion = emotion_predict(rating)
            form.cleaned_data.update({'emotion_predict': emotion, 'rating_predict': rating})
            form.save()
            return render(request, 'reviews/article_detail.html', form.cleaned_data)
        else:
            error = 'Invalid input'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'reviews/create.html', data)
