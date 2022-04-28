import string
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
import numpy as np
import pandas as pd

#word = 'I'
#word_synsets = wn.synsets(word)
#target_synsets = wordnet.synsets(word)
#hypernyms = word_synsets.hypernym_paths()[0]

#print(word_synsets[0].name())
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


#def get_hyponyms(synset):
    #hyponyms = set()
    #for hyponym in synset.hyponyms():
        #hyponyms |= set(get_hyponyms(hyponym))
    #return hyponyms | set(synset.hyponyms)
#
#
##print(syn.name())
##print(syn.definition())
##print(syn.examples())
##print("The hypernyms of color are:" + str(syn.hypernyms()))
##print("The hyponyms of the hypernyms are:" + str(syn.hypernyms()[0].hyponyms()))
##print("The root of the hypernyms is:" + str(syn.root_hypernyms()))
#
#with open('/Users/spicy.kev/Documents/github/henry_james/209-0.txt', encoding='utf-8') as f:
    #data = f.read()
    #tokens = word_tokenize(data)
#
#synonyms = []
#
#for token in tokens:
    #gotten = get_hyponyms(token)
    #if gotten in syn:
        #synonyms.append(gotten)