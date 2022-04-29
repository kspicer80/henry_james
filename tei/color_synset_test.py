import string
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import RegexpTokenizer
import numpy as np
from collections import Counter


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

with open(r'tei\list_of_colors.txt') as f:
	color_word_list = f.read().splitlines()

def get_color_words(text):
    captured_color_words = []
    text = text.lower()
    tokens = word_tokenize(text)
    print(tokens)
    for token in tokens:
        if token in color_word_list:
            captured_color_words.append(token)
    return(captured_color_words)

# Short/Quick Tests:
#test_string ='I hate to go to the store. Black, white, red, and blue are all of my favorite colors. I love them!'

#color_words_in_test_string = get_color_words(test_string)
#print(color_words_in_test_string)

with open(r'C:\Users\KSpicer\Documents\GitHub\henry_james\209-0.txt', encoding='utf-8') as f:
    data = f.read()

found_color_words = get_color_words(data)
print(Counter(found_color_words))
print(len(found_color_words))
