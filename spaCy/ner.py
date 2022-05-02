import spacy
nlp = spacy.load('en_core_web_lg')

file_path = r'.\209-0.txt'
with open(file_path, encoding='utf-8') as f:
    data = f.read()
doc = nlp(data)
print(doc[0:100])

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + '  -  ' + str(ent.start_char) + '  -  '  + str(ent.end_char) + '  -  ' + str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')
        
#doc = nlp('Apple is looking at buying U.K. from Chicago and New York startup for $1 billion in assets.')
#print(show_ents(doc1))

#for e in nlp_file.ents:
    #print(e.text, e.start_char, e.end_char, e.label_)
#entities = [(e.text, e.start_char, e.end_char, e.label_) for e nlp_file.ents]
#print(entities)

#found_entities = show_ents(nlp_file)

print(len([ent for ent in doc.ents if ent.label_ == 'PERSON']))
print([ent for ent in doc.ents if ent.label_ == 'PERSON'])

print(len([ent for ent in doc.ents if ent.label_ == 'GPE' or 'LOC']))
print([ent for ent in doc.ents if ent.label_ == 'GPE' or 'LOC'])
