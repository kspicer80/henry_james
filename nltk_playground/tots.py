import nltk
from nltk.tokenize import word_tokenize
from nltk.draw.dispersion import dispersion_plot
import matplotlib.pyplot as plt
import spacy
nlp = spacy.load('en_core_web_lg')
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
import pandas as pd
import numpy as np

with open('tots.txt', encoding='utf-8') as f:
    data = f.read()

tokens = word_tokenize(data)
tots_text = nltk.Text(tokens)

#prodigious_concordance = tots_text.concordance('prodigious', width=200)
#print(prodigious_concordance)
#portentous_concordance = tots_text.concordance('portentous', width=200)
#sealed_concordance = tots_text.concordance('sealed', width=200)

plt.figure(figsize=(12, 9))
targets=['prodigious', 'prodigiously', 'prodigiousness', 'portentous', 'portentously']
dispersion_plot(tokens, targets, ignore_case=True, title='Lexical Dispersion Plot for "Prodigious" and "Portentous"')

# Using spaCy
#phrase_matcher = PhraseMatcher(nlp.vocab)
#phrases = ['prodigious', 'portentous']
#patterns = [nlp(text) for text in phrases]
#phrase_matcher.add('mhm', None, *patterns)
#
#doc = nlp(data)
#
#for sent in doc.sents:
    #for match_id, start, end in phrase_matcher(nlp(sent.text)):
        #if nlp.vocab.strings[match_id] in ["mhm"]:
            #print(sent.text)

#matcher = Matcher(nlp.vocab)
##pattern_1 = [{'TEXT': 'prodigious'}]
##pattern_2 = [{'TEXT': 'portentous'}]
##matcher.add('mhm', [pattern_1, pattern_2])
#
#lemma_pattern_1 = [{'LEMMA': 'prodigious'}]
#lemma_pattern_2 = [{'LEMMA': 'portenous'}]
#matcher.add('mhm_lemma', [lemma_pattern_1, lemma_pattern_2])
#
#doc = nlp(data)
#matches = matcher(doc)
#print(len(matches))
#for match_id, start, end, in matches:
    #string_id = nlp.vocab.strings[match_id]
    #span = doc[start:end]
    #sents = span.sent
    #print(match_id, string_id, start, end, sents)
#
##print(doc[5013:5014])
#
#def recreate_lexical_dispersion_plot(target, text):
    #return pd.Series(np.histogram(
        #[word.i for word in text if word.text.lower() == target], bins=100)[0])
#
#pd.DataFrame({name: recreate_lexical_dispersion_plot(name.lower(), doc) for name in ['prodigious', 'portentous', 'sealed']}).plot(subplots=True)
#plt.show()
























#from booknlp.booknlp import BookNLP
#
#model_params = {
                #'pipeline': 'entity,quote,supersense,event,coref',
                #'model': 'big'
#}
#
#booknlp = BookNLP('en', model_params)
#
#input_file = 'tots.txt'
#output_directory = 'tots/'
#book_id = 'turn_of_the_screw_omf'
#
#booknlp.process(input_file, output_directory, book_id)
