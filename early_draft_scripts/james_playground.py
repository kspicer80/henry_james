import spacy
nlp = spacy.load('en_core_web_lg')

test_string = '''The story had held us, round the fire, sufficiently breathless, but except the obvious remark that it was gruesome, as, on Christmas Eve in an old house, a strange tale should essentially be, I remember no comment uttered till somebody happened to say that it was the only case he had met in which such a visitation had fallen on a child. The case, I may mention, was that of an apparition in just such an old house as had gathered us for the occasion—an appearance, of a dreadful kind, to a little boy sleeping in the room with his mother and waking her up in the terror of it; waking her not to dissipate his dread and soothe him to sleep again, but to encounter also, herself, before she had succeeded in doing so, the same sight that had shaken him. It was this observation that drew from Douglas—not immediately, but later in the evening—a reply that had the interesting consequence to which I call attention. Someone else told a story not particularly effective, which I saw he was not following. This I took for a sign that he had himself something to produce and that we should only have to wait. We waited in fact till two nights later; but that same evening, before we scattered, he brought out what was in his mind.'''

# Just a silly string to test the lemmatizing that we need here ...
simpler_string = '''I went to the stores to get the store and stores went and go rock and rocks and rocks and rocked and rocking and stores and storing.'''

final_dictionary = {}
lemmas = []
counts = {}

nlp_test_string = nlp(simpler_string)

look_ahead_look_behind = 10

for token in nlp_test_string:
    lemmas.append(token.lemma_)
    lemmas_rejoined = ' '.join(lemmas)
    lemmas_rejoined = lemmas_rejoined.split()

print(len(lemmas_rejoined))

indices = []

for lemma in range(len(lemmas_rejoined)):
    if lemmas[lemma] == lemma:
        indices.append(lemma)

print(indices)



#all_occurences = []
#last_index_found = -1
#element_found = True
#
#for lemma in lemmas_rejoined:
    #while element_found:
        #try:
            #last_found_index = lemmas_rejoined.index(lemma, last_index_found + #1)
            #all_occurences.append(last_found_index)
        #except ValueError:
            #element_found = False
    #if len(all_occurences) == 0:
        #print("Couldn't find it!")
    #else:
        #print("The element was found at index: " + str(all_occurences))

        

#print(lemmas_rejoined)
#for word in lemmas_rejoined:
    #if word 
    #print(word)
        
        #if 
    #enumerated_lemmas = dict(enumerate(lemmas))
    #for k in enumerated_lemmas.keys():
        #final_dictionary[k] = tuple(final_dictionary[k][(token.text, #token.lemma_)] for d in nlp_test_string)
    
    #d = dict((i, token.text, token.lemma_) for i, j, k in enumerated_lemmas)
    #final_dictionary[token.i] = (token.text, token.lemma_)

#print(lemmas)
#print(lemmas_rejoined)
#print(enumerated_lemmas)
#print(d)







#import collections
#
#for token in nlp_test_string:
    #lemma_counts = {}
    #final_dictionary
    #lemmas.append(token.lemma_)
    #for lemma in lemmas:
        #for id in range(len(lemmas)):
            #lemma_counts[id] = (token.text, token.lemma_, #collections.Counter(token.lemma_))
    ##for word, count in sorted(word_counts.items()):
    #print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 0 else #""))
#print(lemma_counts)



#for token in nlp_test_string:
    #lemmas.append(token.lemma_)
    #ids = range(len(lemmas))
    #lemmas_rejoined = ' '.join(lemmas)
    #final_dictionary[token.i] = (token.text, token.lemma_)
    #for lemma in lemmas_rejoined:
        #counts[lemma] = lemmas_rejoined.count(lemma)
        
#print(counts)

#def create_dictionary(text):
    #final_dictionary = dict()
    #lemmas = []
    #counts = {}
    #nlp_text = nlp(text)
    #for token in nlp_text:
        #lemmas.append(token.lemma_)
        #for i in range(len(lemmas)):
            #counts[i] = 
        #final_dictionary[token.i] = (token.text, token.lemma_)

#Following/repurposing from: https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/
def getDuplicatesWithInfo(listOfElems):
    dictOfElems = {}
    index = 0
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
            dictOfElems[elem][1].append(index)
        else:
            dictOfElems[elem] = [1, [index]]
        index += 1
    dictOfElems = {key: value for key, value in dictOfElems.items() if value[0]>1}
    return dictOfElems

#dictOfElements = getDuplicatesWithInfo(lemmas_rejoined)

#for key, value in dictOfElements.items():
    #print('Element = ', key, ':: Repeated Count = ', value[0], ':: Index Positions = ', value[1])

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
