from collections import defaultdict
from collections import Counter
from more_itertools import pairwise
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
import spacy
nlp = spacy.load('en_core_web_lg')
spacy_stopwords = nlp.Defaults.stop_words

#with open('209-0.txt', encoding='utf-8') as f:
    #data = f.read()

test_string = '''The story had held us, round the fire, sufficiently breathless, but except the obvious remark that it was gruesome, as, on Christmas Eve in an old house, a strange tale should essentially be, I remember no comment uttered till somebody happened to say that it was the only case he had met in which such a visitation had fallen on a child. The case, I may mention, was that of an apparition in just such an old house as had gathered us for the occasion—an appearance, of a dreadful kind, to a little boy sleeping in the room with his mother and waking her up in the terror of it; waking her not to dissipate his dread and soothe him to sleep again, but to encounter also, herself, before she had succeeded in doing so, the same sight that had shaken him. It was this observation that drew from Douglas—not immediately, but later in the evening—a reply that had the interesting consequence to which I call attention. Someone else told a story not particularly effective, which I saw he was not following. This I took for a sign that he had himself something to produce and that we should only have to wait. We waited in fact till two nights later; but that same evening, before we scattered, he brought out what was in his mind.'''

#def find_repetitions(text):
    #nlp_text = nlp(text)
    #sentences = []
    #lemmas = []
    #dictOfElems = dict()
    #index = 0
    #for sent in nlp_text.sents:
        #for token in sent:
            #lemmas.append((token.text, token.i - sent.start))
        #for elem in lemmas:
            #if elem in dictOfElems:
                #dictOfElems[elem][0] += 1
                #dictOfElems[elem][1].append(index)
            #else:
                #dictOfElems[elem] = [1, [index]]
            #index += 1
    #dictOfElems = {key: value for key, value in dictOfElems.items() if value[0]>1}
    #return dictOfElems

def keep_sentence_index_numbers(text):
    nlp_text = nlp(text)
    lemmas = []
    test_dict = defaultdict(list)
    dictOfElems = defaultdict(list)
    index = 0
    for sent_index, sent in enumerate(nlp_text.sents):
        for token in sent:
            for elem in test_dict.keys():
                if elem in test_dict.keys():
                    test_dict[elem.lemma_] = [token.idx, sent_index, token.i-sent.start]
                    test_dict[elem.lemma_][0] += 1
                    test_dict[elem.lemma_][1].append(elem.idx)
                else:
                    dictOfElems[elem] = [1, [elem.idx]]
                index += 1
    dictOfElems = {key: value for key, value in dictOfElems.items() if value[0]>1}
    return(test_dict)

test_string_1 = '''I went to the store today. I ran and ran all the way until I couldn't run anymore. Then I went to the store again. I hate the store!'''

def index_sentences(text):
    nlp_text = nlp(text)
    sent_dict = defaultdict(list)
    for sent_index, sent in enumerate(nlp_text.sents):
        sent_dict[sent_index] = []


def find_repetitions(text):
    nlp_text = nlp(text)
    lemmas = []
    dictOfElems = dict()
    index = 0
    text_no_punct = [token for token in nlp_text if not token.is_punct and token not in spacy_stopwords]
    for sent_index, sent in enumerate(nlp_text.sents):
        tokens = [token for token in sent]
        for token_index, token in enumerate(tokens):
            #print(token.text)
            #test_dict[token.text] = [sent_index, token.i-sent.start, token.lemma_]
            lemmas.append([sent_index, token.i, token.i-sent.start, token.text, token.lemma_])
    return lemmas

#repetitions = find_repetitions(test_string_1)
#print(repetitions)


test_list = [1, 2, 3, 1, 2, 1, 5, 6, 7, 8, 9]

def find_repetitions_version_two(text):
    nlp_text = nlp(text)
    sentence_dict = defaultdict(list)
    for sent_index, sentence in enumerate(nlp_text.sents):
        for token in sentence:
            sentence_dict[token.lemma_] = [token.text, token.idx, token.idx-sentence.start, sentence]


    for element in sentence_dict.keys():
        if element in sentence_dict:
            sentence_dict[element][0] += 1
            sentence_dict[element][1].append(element.idx)
        else:
            sentence_dict[element] = [1, [element.idx]]
        index += 1
    #freq = {key: value for key, value in freq.items() if value[0]>1}
    return freq

#version_two_test = find_repetitions_version_two(test_string_1)
#print(version_two_test)

def repetitions(text):
    nlp_text = nlp(text)
    test_dict = defaultdict()
    runninglist = []
    index = 0
    for sent_index, sent in enumerate(nlp_text.sents):
        for token in sent:
            runninglist.append([token.lemma_, token.i, token.i-sent.start, sent_index])
            for element in runninglist[0]:
                test_dict[element][0] += 1
                test_dict[element].append(index)
            else:
                test_dict[key].append([1, [index]])
            index += 1
    #test_dict = {key: value for key, value in dictOfElems.items() if value[0]>1}
    return(test_dict)

test = repetitions(test_string_1)
print(test)


#for elem in lemmas:
    #if elem in dictOfElems:
        #dictOfElems[elem][0] += 1
        #dictOfElems[elem][1].append(index)
    #else:
        #dictOfElems[elem] = [1, [index]]
    #index += 1








# Keeping track of sentence numbers ...? https://stackoverflow.com/questions/50742516/how-to-get-the-index-of-a-token-in-a-sentence-in-spacy
#for sent_index, sentence in enumerate(spacy_text.sents):
    #for token in sentence:
        #test_dict[sent_index] = (token.text, token.i - sentence.start)
#print(test_dict)
