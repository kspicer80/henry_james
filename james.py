import spacy
nlp = spacy.load('en_core_web_lg')

test_string = '''The story had held us, round the fire, sufficiently breathless, but except the obvious remark that it was gruesome, as, on Christmas Eve in an old house, a strange tale should essentially be, I remember no comment uttered till somebody happened to say that it was the only case he had met in which such a visitation had fallen on a child. The case, I may mention, was that of an apparition in just such an old house as had gathered us for the occasion—an appearance, of a dreadful kind, to a little boy sleeping in the room with his mother and waking her up in the terror of it; waking her not to dissipate his dread and soothe him to sleep again, but to encounter also, herself, before she had succeeded in doing so, the same sight that had shaken him. It was this observation that drew from Douglas—not immediately, but later in the evening—a reply that had the interesting consequence to which I call attention. Someone else told a story not particularly effective, which I saw he was not following. This I took for a sign that he had himself something to produce and that we should only have to wait. We waited in fact till two nights later; but that same evening, before we scattered, he brought out what was in his mind.'''

# Just a silly string to test the lemmatizing that we need here ...
simpler_string = '''I went to the stores to get the store and stores went and go rock and rocks and rocks and rocked and rocking and stores and storing.'''

final_dictionary = {}
lemmas = []
counts = {}

nlp_test_string = nlp(test_string)

look_ahead_look_behind = 10

for token in nlp_test_string:
    lemmas.append(token.lemma_)
    lemmas_rejoined = ' '.join(lemmas)
    lemmas_rejoined = lemmas_rejoined.split()

print(lemmas_rejoined)

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

dictOfElements = getDuplicatesWithInfo(lemmas_rejoined)

for key, value in dictOfElements.items():
    print('Element = ', key, ':: Repeated Count = ', value[0], ':: Index Positions = ', value[1])
