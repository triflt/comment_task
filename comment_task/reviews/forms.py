from .models import Article
from django.forms import ModelForm, TextInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'review']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Film name'
            }),
            "review": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Film review'
            })

        }
