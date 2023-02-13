import os
import re

import numpy as np
import pickle

from tqdm import tqdm
from gensim.models import Word2Vec
from gensim.utils import tokenize


model_wv = Word2Vec.load('../models/trained_word2vec.model')

model_reg = pickle.load(open('../models/cb_reg.model', "rb"))


def sent2vec_generate(question: str):
    dim = model_wv.vector_size
    token_question = np.array(list(tokenize(question, lowercase=True, deacc=True)))
    question_array = np.zeros(dim)
    count = 0
    for word in token_question:
        if model_wv.wv.__contains__(str(word)):
            question_array += (np.array(model_wv.wv[str(word)]))
            count += 1
    if count == 0:
        return question_array

    return question_array / count


def rating_predict(vector):
    predict = model_reg.predict(vector)

    '''def remake(x):
        flag = -1 if x < 5 else 1
        threshold = 5 if x < 5 else 11
        x += flag * (threshold - x) * 0.5
        if x < 1:
            return 1
        if x > 10:
            return 10
        return x'''

    return predict


def emotion_predict(rating):
    return 'positive :)' if rating >= 6 else 'negative :('

"""vec = sent2vec_generate('I was prepared for a turgid talky soap opera cum travelogue, '
                        'but was pleased to find a fast-paced script, an underlying moral,'
                        ' excellent portrayals from all the actors, especially Peter Finch,'
                        ' amazing special effects, suspense, and beautiful cinematography--'
                        'theres even a shot of the majestic stone Buddhas recently destroyed by the Taliban. '
                        'Not to mention Elizabeth Taylor at her most gloriously beautiful and sympathetic,'
                        ' before she gave in to the gaspy hysterics that marred her later work.'
                        ' All the supporting players round it out, and I do wonder who trained all those elephants.', model_wv)

rating = rating_predict(vec)
emotion = emotion_predict(rating)
print(rating)
print(emotion)"""
