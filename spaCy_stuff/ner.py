import re
from collections import Counter
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_lg')

#windows_file_path = r'.\209-0.txt'
#mac_file_path = '../209-0.txt'
#with open(mac_file_path, encoding='utf-8') as f:
    #data = f.read()
#doc = nlp(data)
#print(doc[0:100])

test_string = '''
The story had held us, round the fire, sufficiently breathless, but
except the obvious remark that it was gruesome, as, on Christmas Eve in
an old house, a strange tale should essentially be, I remember no
comment uttered till somebody happened to say that it was the only case
he had met in which such a visitation had fallen on a child. The case,
I may mention, was that of an apparition in just such an old house as
had gathered us for the occasion—an appearance, of a dreadful kind, to
a little boy sleeping in the room with his mother and waking her up in
the terror of it; waking her not to dissipate his dread and soothe him
to sleep again, but to encounter also, herself, before she had
succeeded in doing so, the same sight that had shaken him. It was this
observation that drew from Douglas—not immediately, but later in the
evening—a reply that had the interesting consequence to which I call
attention. Someone else told a story not particularly effective, which
I saw he was not following. This I took for a sign that he had himself
something to produce and that we should only have to wait. We waited in
fact till two nights later; but that same evening, before we scattered,
he brought out what was in his mind.
'''

#time_entities = [ent for ent in doc.ents if ent.label_ == 'TIME']
#test_string = ' '.join(t.text if t.ent_type_)
#print(time_entities)

time_label_open = '<time>'
time_label_close = '</time>'

date_label_open = '<date>'
date_label_close = '</date>'
            
#if ent.label == 'DATE':
    #new_string = new_string = date_label_open + new_string[:start] + ent.text + new_string[end:] + date_label_close

doc = nlp(test_string)

def show_ents(doc):
    keepers = []
    for token in doc:
        for token in doc.ents:
            if token.label_ == 'TIME':
                keepers.append(time_label_open + token.text + time_label_close)
    else:
        pass
    return keepers

replaced = show_ents(doc)
print(' '.join(replaced))
#doc = nlp('Apple is looking at buying U.K. from Chicago and New York startup for $1 billion in assets.')
#print(show_ents(doc1))

#for e in nlp_file.ents:
    #print(e.text, e.start_char, e.end_char, e.label_)
#entities = [(e.text, e.start_char, e.end_char, e.label_) for e nlp_file.ents]
#print(entities)

#found_entities = show_ents(nlp_file)

#print(len([ent for ent in doc.ents if ent.label_ == 'PERSON']))
#print([ent for ent in doc.ents if ent.label_ == 'PERSON'])
#
#print(len([ent for ent in doc.ents if ent.label_ == 'GPE' or 'LOC']))
#print([ent for ent in doc.ents if ent.label_ == 'GPE' or 'LOC'])
#
#ents = Counter()
#
#for ent in doc.ents:
    #ents[f"{ent.label_}:{ent.text}"] += 1
#
#for key, val in ents.items():
    #print(val, key, sep="\t")

#displacy.serve(doc, style='ent', options=options)
