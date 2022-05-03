import pandas as pd
pd.set_option('display.max_colwidth', 800)
import numpy as np
import matplotlib.pyplot as plt
import spacy

OPEN_DATA_URL = '../209-0.txt'
f=open(OPEN_DATA_URL,'r',encoding='utf-8')
text=f.read()
f.close()
import re

HANDLE = '@\w+'
LINK = 'https?://t\.co/\w+'
SPECIAL_CHARS = '&lt;|&lt;|&amp;|#'
PARA='\n+'
def clean(text):
    text = re.sub(LINK, ' ', text)
    text = re.sub(SPECIAL_CHARS, ' ', text)
    text = re.sub(PARA, '\n', text)
    return text
text = clean(text)
text

nlp = spacy.load('en_core_web_lg')
doc=nlp(text)
pos_list=['NOUN']
preproc_text=[]
preproc_sent=[]
for token in doc:
    if token.text!='\n':
        if not(token.is_stop) and not(token.is_punct) \
        and token.pos_ in pos_list:
            preproc_sent.append(token.lemma_)
    else:
        preproc_text.append(preproc_sent)

import tomotopy as tp
mdl = tp.HDPModel(min_cf=5,seed=0)
for line in preproc_text:
    mdl.add_doc(line)
for i in range(0, 100, 10):
    mdl.train(i)
    print('Iteration: {}\tLog-likelihood: {}'.\
          format(i, mdl.ll_per_word))
for k in range(mdl.k):
    print('Top 10 words of topic #{}'.format(k))
    print(mdl.get_topic_words(k, top_n=7))