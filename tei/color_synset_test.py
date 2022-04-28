import string
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
import numpy as np
import pandas as pd

#word = 'I'
#syn = wn.synsets(word)
#target_synsets = wn.synsets(word)
#hypernyms = syn.hypernym_paths()[0]

#print(syn[0].name())
#print(syn.name())
#print(syn.definition())
#print(syn.examples())
#print("The hypernyms of color are:" + str(syn.hypernyms()))
#print("The hyponyms of the hypernyms are:" + str(syn.hypernyms()[0].hyponyms()))
#print("The root of the hypernyms is:" + str(syn.root_hypernyms()))

def convert_tag(tag):
    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None

def doc_to_synsets(doc):
    tokens = nltk.word_tokenize(doc)
    pos = nltk.pos_tag(tokens)
    tags = [tag[1] for tag in pos]
    wntag = [convert_tag(tag) for tag in tags]
    ans = list(zip(tokens, wntag))
    sets = [wn.synsets(x, y) for x, y in ans]
    final = [val[0] for val in sets if len(val) > 0]
    return final

#print(target_synsets)

test_string = "I hate to go to the store. Black, white, red, and blue are all of my favorite colors. I love them!"

test = doc_to_synsets(test_string)
print(test)
