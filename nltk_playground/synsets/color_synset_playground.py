import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import RegexpTokenizer
import numpy as np
from collections import Counter

color = wn.synsets('color')
print(color)

color_hypernyms = color.hypernyms() 
color_hyponyms = color.hyponyms()
syn_lemmas = wn.synset('color.n.01').lemmas()

print(color_hypernyms)
print(color_hyponyms)
print(syn_lemmas)
