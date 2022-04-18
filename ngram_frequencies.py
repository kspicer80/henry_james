import nltk
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from collections import Counter
import operator
from functools import reduce
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_lg')
spacy_stopwords = nlp.Defaults.stop_words

with open('209-0.txt', encoding='utf-8') as f:
    data = f.read()

def compute_freq(sentence, n_value=4):
    tokens = nltk.word_tokenize(sentence)
    ngrams = nltk.ngrams(tokens, n_value)
    ngram_fdist = nltk.FreqDist(ngrams)
    return ngram_fdist

four_gram_frequencies = compute_freq(data)
print(four_gram_frequencies)

dictionary = {k: v for k, v in sorted(four_gram_frequencies.items(), key=lambda item: item[1])}
#for k, v in four_gram_frequencies.items():
    #print(k, v)
    
df = pd.DataFrame.from_dict(dictionary, orient='index')
print(df.head(50))
