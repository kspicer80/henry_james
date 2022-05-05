import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_lg')

s = "His friend Nicolas and Joseph is as well; he is also here—and don't forget that we're traveling to Chicago tomorrow morning."
doc = nlp(s)

person_open = '<person>'
person_close = '</person>'

replaced = []
for token in doc:
    if token.ent_type_ == 'PERSON':
        new_token = person_open + token.text + person_close
        replaced.append(new_token)
    else: 
        replaced.append(token)
        

print([t.text if not t.ent_type_ else t.ent_type_ for t in doc])
# ['His', 'friend', 'PERSON', 'is', 'here', '.']

#print(" ".join([t.text if not t.ent_type_ else t.ent_type_ for t in doc]) )
# His friend PERSON is here .

print(type(replaced))
print(' '.join(str(v) for v in replaced))
