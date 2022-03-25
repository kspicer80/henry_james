from more_itertools import pairwise
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_lg')

#test_string = '''The story had held us, round the fire, sufficiently breathless, but except the obvious remark that it was gruesome, as, on Christmas Eve in an old house, a strange tale should essentially be, I remember no comment uttered till somebody happened to say that it was the only case he had met in which such a visitation had fallen on a child. The case, I may mention, was that of an apparition in just such an old house as had gathered us for the occasion—an appearance, of a dreadful kind, to a little boy sleeping in the room with his mother and waking her up in the terror of it; waking her not to dissipate his dread and soothe him to sleep again, but to encounter also, herself, before she had succeeded in doing so, the same sight that had shaken him. It was this observation that drew from Douglas—not immediately, but later in the evening—a reply that had the interesting consequence to which I call attention. Someone else told a story not particularly effective, which I saw he was not following. This I took for a sign that he had himself something to produce and that we should only have to wait. We waited in fact till two nights later; but that same evening, before we scattered, he brought out what was in his mind.'''

# Just a silly string to test the lemmatizing that we need here ...
#simpler_string = '''I went to the stores to get the store and stores went and go rock and rocks and rocks and rocked and rocking and stores and storing.'''

with open(r'C:\Users\KSpicer\Documents\GitHub\henry_james\209-0.txt', encoding ='utf-8') as f:
    data = f.read()

spacy_text = nlp(data)

#Following/repurposing from: https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/
def find_repetitions(text):
    lemmas = []
    dictOfElems = dict()
    index = 0
    for token in text:
        lemmas.append(token.lemma_)
    for elem in lemmas:
        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
            dictOfElems[elem][1].append(index)
        else:
            dictOfElems[elem] = [1, [index]]
        index += 1
    dictOfElems = {key: value for key, value in dictOfElems.items() if value[0]>1}
    return dictOfElems

# Let's right a function to find the indices that are a specific number away from one another—following one of the anwsers proposed at https://stackoverflow.com/questions/23541567/find-numbers-in-python-list-which-are-within-a-certain-distance-of-each-other/39814970
def find_neighbors(list, close_number=int()):
    results = []
    chunk = []
    list.sort()
    for n1, n2 in pairwise(list):
        if n2 - n1 <= close_number:
            chunk.append(n1)
        elif chunk:
            chunk.append(n1)
            results.append(chunk)
            chunk = []
    return(results)
            
repetitions = find_repetitions(spacy_text)
#print(repetitions)

df = pd.DataFrame(repetitions)
df = df.T
df = df.rename(columns={0: 'number_of_repetitions', 1: 'indices'})
print(df.head())
#print(df.columns)
df.to_csv('repetition_counts.csv')
