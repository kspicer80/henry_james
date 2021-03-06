from pathlib import Path
import re
from collections import Counter
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_lg')

path = Path('209-0.txt')
#print(path)
#print(path.home())
#print(path.exists())
#print(path.is_file())
#print(path.is_dir())
#print(path.suffix)
#print(path.stem)
#print(path.parent)
#print(path.absolute())

with open(path, encoding='utf-8') as f:
    data = f.read()
doc = nlp(data)
#print(doc[:100])
#
#def show_ents(doc):
    #if doc.ents:
        #for ent in doc.ents:
            #print(ent.text + '  -  ' + str(ent.start_char) + '  -  ' + str(ent.end_char) + '  -  ' + ent.label_ + '  -  ' + #str(spacy.explain*(ent.label_)))
            
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
ents = Counter()

for ent in doc.ents:
    ents[f"{ent.label_}:{ent.text}"] += 1

print(ents)
#for key, val in ents.items():
    #print(val, key, sep="\t")

#displacy.serve(doc, style='ent', options=options)
