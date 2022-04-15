from more_itertools import pairwise
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
import spacy
nlp = spacy.load('en_core_web_lg')
spacy_stopwords = nlp.Defaults.stop_words

with open('209-0.txt', encoding='utf-8') as f:
    data = f.read()

test_string = '''The story had held us, round the fire, sufficiently breathless, but except the obvious remark that it was gruesome, as, on Christmas Eve in an old house, a strange tale should essentially be, I remember no comment uttered till somebody happened to say that it was the only case he had met in which such a visitation had fallen on a child. The case, I may mention, was that of an apparition in just such an old house as had gathered us for the occasion—an appearance, of a dreadful kind, to a little boy sleeping in the room with his mother and waking her up in the terror of it; waking her not to dissipate his dread and soothe him to sleep again, but to encounter also, herself, before she had succeeded in doing so, the same sight that had shaken him. It was this observation that drew from Douglas—not immediately, but later in the evening—a reply that had the interesting consequence to which I call attention. Someone else told a story not particularly effective, which I saw he was not following. This I took for a sign that he had himself something to produce and that we should only have to wait. We waited in fact till two nights later; but that same evening, before we scattered, he brought out what was in his mind.'''

def find_repetitions(text):
    nlp_text = nlp(text)
    sentences = []
    lemmas = []
    dictOfElems = dict()
    index = 0
    for sent in nlp_text.sents:
        for token in sent:
            lemmas.append((token.text, token.i - sent.start))
        for elem in lemmas:
            if elem in dictOfElems:
                dictOfElems[elem][0] += 1
                dictOfElems[elem][1].append(index)
            else:
                dictOfElems[elem] = [1, [index]]
            index += 1
    dictOfElems = {key: value for key, value in dictOfElems.items() if value[0]>1}
    return dictOfElems

#result = find_repetitions(test_string)
#print(result)

#df = pd.DataFrame(result)
#print(df.head(50))
#print(df.columns)
#df = df.T
#print(df.head(25))
#df = df.unstack(level=0)
#df.columns = df.columns.droplevel()
#df = df.rename(columns={0: 'number_of_repetitions', 1: 'indices'})
#print(df)
#df.to_csv('with_sentence_indexing.csv')

test_dict = {}
spacy_text = nlp(test_string)
for sent_index, sent in enumerate(spacy_text.sents):
    for token in sent:
        print(sent_index, token.i - sent.start, token.text)

# Keeping track of sentence numbers ...? https://stackoverflow.com/questions/50742516/how-to-get-the-index-of-a-token-in-a-sentence-in-spacy
#for sent_index, sentence in enumerate(spacy_text.sents):
    #for token in sentence:
        #test_dict[sent_index] = (token.text, token.i - sentence.start)
#print(test_dict)
