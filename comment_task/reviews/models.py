from django.db import models


class Article(models.Model):
    name = models.CharField('Name', max_length=50)
    review = models.TextField('Review')
    emotion_predict = models.CharField('Predict target', max_length=10, null=True)
    rating_predict = models.IntegerField('Predict rating', null=True)

    def __str__(self):
        return self.name
